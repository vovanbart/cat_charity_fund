from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_project_by_name(
            self,
            project_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        project_name = await session.execute(
            select(CharityProject).where(
                CharityProject.name == project_name
            )
        )
        project_name = project_name.scalars().first()
        return project_name


charity_project_crud = CRUDCharityProject(CharityProject)
