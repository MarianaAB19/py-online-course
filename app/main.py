class OnlineCourse:

    course_dict = {}

    def __init__(self, name: str, description: str,
                 weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks
        OnlineCourse.course_dict["name"] = self.name
        OnlineCourse.course_dict["description"] = self.description
        OnlineCourse.course_dict["days"] = None

    @staticmethod
    def days_to_weeks(days: int) -> int:
        if days % 7 == 0:
            return days / 7
        return days // 7 + 1

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        return cls(course_dict["name"], course_dict["description"],
                   OnlineCourse.days_to_weeks(course_dict["days"]))
