import os.path
import unittest
from lecture_12.homework_10 import log_event


class TestLogEvent(unittest.TestCase):
    def test_log_event_creates_file(self):
        log_event('user', 'success')
        self.assertTrue(os.path.isfile('login_system.log'))

    def test_log_event(self):
        with self.assertLogs('log_event', level='INFO') as logger:
            log_event('user', 'success')
            log_event('user', 'expired')
            log_event('user', 'error')
        self.assertEqual(
            logger.output, ['INFO:log_event:Login event - Username: user, Status: success',
                            'WARNING:log_event:Login event - Username: user, Status: expired',
                            'ERROR:log_event:Login event - Username: user, Status: error'
                            ]
        )


if __name__ == '__main__':
    unittest.main()
