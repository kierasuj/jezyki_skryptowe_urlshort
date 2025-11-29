import threading
from typing import Type, Any


def singleton(cls: Type[Any]) -> Type[Any]:
    """
    Class decorator to make any class a thread-safe singleton and inject
    a `get_instance()` classmethod for accessing the singleton.

    Usage:
        @singleton
        class MyService:
            ...

        svc = MyService.get_instance()
    """
    lock = threading.Lock()
    _instance_attr = "_singleton_instance"

    # Ensure no name collision
    if hasattr(cls, _instance_attr):
        raise AttributeError(f"{cls.__name__} already defines '{_instance_attr}'")

    setattr(cls, _instance_attr, None)

    @classmethod
    def get_instance(inner_cls, *args, **kwargs):
        # Double-checked locking
        if getattr(inner_cls, _instance_attr) is None:
            with lock:
                if getattr(inner_cls, _instance_attr) is None:
                    instance = inner_cls(*args, **kwargs)  # type: ignore[misc]
                    setattr(inner_cls, _instance_attr, instance)
        return getattr(inner_cls, _instance_attr)

    # Attach the accessor
    setattr(cls, "get_instance", get_instance)
    return cls


# Backward compatibility: keep Decorators.singleton alias for older imports
class Decorators:
    """Deprecated: use `@singleton` instead of `@Decorators.singleton`."""

    @staticmethod
    def singleton(cls: Type[Any]) -> Type[Any]:
        return singleton(cls)