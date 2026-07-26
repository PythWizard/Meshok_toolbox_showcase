"""
Meshok Toolbox
Desktop marketplace automation prototype

Demonstrates:
- Async API integration
- User filtering pipeline
- Local dataset storage
- Browser session integration
- Automated messaging workflow
"""

import asyncio
import json
import random
from datetime import datetime, timezone

import aiohttp


API_INFO_URL = (
    "https://meshok.net/api/command/sellers/get-aggregated-info"
)

API_MESSAGE_URL = (
    "https://meshok.net/api/command/forum/send-forum-message-v2"
)


class MeshokScanner:
    """
    Async marketplace user scanner.
    """

    def __init__(self):
        self.results = []


    async def fetch_user(self, session, user_id):
        """
        Retrieve marketplace user information.
        """

        async with session.post(
            API_INFO_URL,
            json={"userId": user_id}
        ) as response:

            if response.status != 200:
                return None

            data = await response.json()

            return data.get("result")


    def apply_filters(self, user):
        """
        Filtering engine.
        """

        if user.get("lotsCount", 0) < 10:
            return False

        if user.get("isDeleted"):
            return False

        return True


    async def scan(self, start_id, end_id):

        connector = aiohttp.TCPConnector(limit=20)

        async with aiohttp.ClientSession(
            connector=connector
        ) as session:

            for user_id in range(start_id, end_id):

                user = await self.fetch_user(
                    session,
                    user_id
                )

                if not user:
                    continue


                if self.apply_filters(user):

                    self.results.append(
                        {
                            "id": user_id,
                            "name": user.get(
                                "displayName"
                            ),
                            "lots": user.get(
                                "lotsCount"
                            )
                        }
                    )


                await asyncio.sleep(
                    random.uniform(
                        0.05,
                        0.2
                    )
                )


        self.save()


    def save(self):

        with open(
            "results.json",
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.results,
                file,
                indent=4,
                ensure_ascii=False
            )


class MessageSender:
    """
    Automated marketplace communication module.
    """


    def __init__(self, cookies):
        self.cookies = cookies


    async def send_message(
        self,
        session,
        user_id,
        message
    ):

        payload = {
            "messageBody": message,
            "forumId": {
                "entityId": user_id,
                "entityType": "u"
            }
        }


        async with session.post(
            API_MESSAGE_URL,
            json=payload
        ) as response:

            return response.status == 200



async def main():

    scanner = MeshokScanner()

    await scanner.scan(
        100000,
        101000
    )


    print(
        f"Found users: {len(scanner.results)}"
    )


if __name__ == "__main__":

    asyncio.run(main())
