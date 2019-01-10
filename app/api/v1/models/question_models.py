import datetime

question = []

question_id = 1

class Questions():

    def post_question(self, createdOn, createdby, meetup_id, title, body, votes):
        new_question = dict(
            question_id = len(question) + 1,
            createdOn = datetime.datetime.now().strftime("%H:%M%P %A %d %B %Y"),
            createdBy = createdby,
            meetup_id = meetup_id,
            title = title,
            body = body,
            votes = 0
        )

        question.append(new_question)
        return new_question