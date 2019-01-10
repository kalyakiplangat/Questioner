from flask import Flask, request, jsonify, Blueprint, json, make_response
from flask_restplus import Resource, reqparse, Namespace, fields, Api

from ...v1.models import question_models

parser = reqparse.RequestParser()
parser.add_argument("createdOn", help="This field cannot be blank")
parser.add_argument("createdBy", help="This field cannot be blank")
parser.add_argument("meetup_id", help="This field is optional")
parser.add_argument("title", help="This field cannot be blank")
parser.add_argument("body", help="This field cannot be blank")
parser.add_argument("votes", help="This field cannot be blank")

question = Namespace("questions", description="Question endpoints")

mod_post_question = question.model("Post a new question", {
    "createdOn": fields.String("Date question was posted"),
    "createdBy": fields.Integer("User id of member who posted it"),
    "meetup_id": fields.Integer("ID of meetup where the question is posted"),
    "title": fields.String("Title of the question"),
    "body": fields.String("Body/content of the question"),
    "votes": fields.Integer("Number of votes the question has received")
})

@question.route("")
class PostQuestion(Resource):
    @question.doc(security="apikey")
    @question.expect(mod_post_question)

    def post(self):
        args = parser.parse_args()
        createdOn = args["createdOn"]
        createdBy = args["createdBy"]
        meetup_id = args["meetup_id"]
        title = args["title"]
        body = args["body"]
        votes = args["votes"]
