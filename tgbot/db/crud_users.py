from datetime import date
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from tgbot.db.models import UserModel


class UserCrud:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_user(
        self,
        user_id: int,
        user_name: str,
        create_date: Optional[date],
        day: int,
    ):
        user = UserModel(
            user_id=user_id,
            user_name=user_name,
            create_date=create_date,
            day=day,
        )

        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def get_users_list(self):
        result = await self.session.execute(select(UserModel))
        return result.scalars().all()

    async def get_user(self, user_id: int):
        result = await self.session.execute(
            select(UserModel).where(UserModel.user_id == user_id)
        )
        return result.scalar_one_or_none()
