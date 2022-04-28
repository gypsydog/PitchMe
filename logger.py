import logging
from contextlib import contextmanager

import allure


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
log = logging.getLogger()


@contextmanager
def step(desc: str) -> str:
    log.info(f'STEP {desc}')
    with allure.step(desc) as s:
        yield s
