# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.
from service.basic import BasicService


class MovieService(BasicService):
    def get_all_by_filter(self, *args, **kwargs):
        return self.dao.get_all_by_filter(*args, **kwargs)
