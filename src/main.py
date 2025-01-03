from asyncio import Runner

from loguru import logger


async def main() -> None:
    logger.info('Hello, World!')


if __name__ == '__main__':
    Runner().run(main())
