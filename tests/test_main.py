import asyncio
from datetime import datetime, timezone
import unittest

from main import get_current_time


class GetCurrentTimeTest(unittest.TestCase):
    def test_returns_iso_datetime(self):
        data = asyncio.run(get_current_time())
        self.assertIn("time", data)
        # Ensure the time can be parsed as an ISO formatted datetime
        datetime.fromisoformat(data["time"])

    def test_time_is_current_to_the_second(self):
        before = datetime.now(tz=timezone.utc).replace(microsecond=0)
        data = asyncio.run(get_current_time())
        returned_time = datetime.fromisoformat(data["time"]).replace(microsecond=0)
        after = datetime.now(tz=timezone.utc).replace(microsecond=0)

        self.assertTrue(before <= returned_time <= after)
