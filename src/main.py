import asyncio
from viam.module.module import Module
try:
    from models.lamp_alarm import LampAlarm
except ModuleNotFoundError:
    # when running as local module with run.sh
    from .models.lamp_alarm import LampAlarm


if __name__ == '__main__':
    asyncio.run(Module.run_from_registry())
