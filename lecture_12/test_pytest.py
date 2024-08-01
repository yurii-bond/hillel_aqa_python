import logging


from lecture_12.homework_10 import log_event


LOGGER = logging.getLogger(__name__)


def test_log_event(caplog):
    LOGGER.info('Check log event')
    caplog.set_level(logging.INFO)
    log_event('user', 'success')
    assert 'INFO     log_event:homework_10.py:38 Login event - Username: user, Status: success\n' in caplog.text


def test_log_event_with_caplog(caplog):
    with caplog.at_level(logging.INFO):
        log_event('user', 'success')
    assert 'INFO     log_event:homework_10.py:38 Login event - Username: user, Status: success\n' in caplog.text
