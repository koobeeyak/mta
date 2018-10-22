# project
from app import db
from common import StatusTypes
from common.utils import increment_time_delayed
from models.line import Line as SQLLine
from process.status_fetcher import StatusFetcher
from process.line import Line


class UpdateLines(object):
    def update(self, new_line):
        """
        :type new_line: Line
        """
        db_line = SQLLine.query.get(new_line.name)
        if new_line.status == StatusTypes.DELAYED:
            if db_line.status == StatusTypes.NOT_DELAYED:
                print("Line {} is experiencing delays.".format(db_line.name))  # todo should be logged
                db_line.time_delayed = increment_time_delayed(db_line.time_delayed)
        elif new_line.status == StatusTypes.NOT_DELAYED:
            if db_line.status == StatusTypes.DELAYED:
                print("Line {} is now recovered.".format(db_line.name))
        db_line.status = new_line.status
        db.session.commit()

    def run(self):
        lines = StatusFetcher().run()
        [self.update(line) for line in lines]


if __name__ == '__main__':
    UpdateLines().run()
