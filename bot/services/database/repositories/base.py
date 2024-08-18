from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository:
    _session: AsyncSession

    def __init__(self, session: AsyncSession):
        self._session = session

    @property
    def session(self):
        return self._session
