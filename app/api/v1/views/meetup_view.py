from flask import Flask, request, jsonify, Blueprint, json, make_response
from flask_restplus import Api, Resource, reqparse, Namespace, fields

from ...v1.models import meetup_model
from ...v1.models import user_models


parser = reqparse.RequestParser()
parser.add_argument("createdOn", help="This field cannot be blank")
parser.add_argument("location", help="This field cannot be blank")
parser.add_argument("images", help="This field is optional")
parser.add_argument("topic", help="This field cannot be blank")
parser.add_argument("happeningOn", help="This field cannot be blank")
parser.add_argument("Tags", help="This field cannot be blank")


meetups = Namespace("meetups", description="Meetups endpoints")
mod_create = meetups.model("Create a new meetup", {
    "createdOn":fields.String("Date meetup was created"),
    "location":fields.String("Location of the meetup"),
    "images":fields.String("URL of the images"),
    "topic":fields.String("Topic to be discussed"),
    "happeningOn":fields.String("Date the meetup is happening"),
    "Tags":fields.String("Tags associated with this meetup")
})


@meetups.route('')
class CreateMeetup(Resource):
    @meetups.doc(security="apikey")
    @meetups.expect(mod_create)
    def post(self):
        args = parser.parse_args()
        createdOn = args["createdOn"]
        location = args["location"]
        images = args["images"]
        topic = args["topic"]
        happeningOn = args["happeningOn"]
        Tags = args["Tags"]

        meetups = meetup_model.Meetups().create_meetup(createdOn, location, images, topic, happeningOn, Tags)
        return {
        
            "status": 201,
            "message": "New meetup created successfully",
            "data": meetups,
            }, 201
        

    
@meetups.route('/upcoming')
class GetAllMeetups(Resource):
    @meetups.doc(security="apikey")
    def get(self):
        all_meetups = meetup_model.meetup
        if len(all_meetups) == 0:
            return {
                "status": 404,
                "error": "No meetups found"
                }, 404

        return {
                "status": 200,
                "data": all_meetups
            }, 200


@meetups.route("/<int:meetup_id>")
class GetMeetupById(Resource):
    @meetups.doc(security="apikey")
    def get(self, meetup_id):
        single_meetup = meetup_model.Meetups.get_specific_meetup(meetup_id)
        if single_meetup:
            return {
                "status": 200,
                "data": single_meetup
            }, 200
        return {
            "status": 404,
            "response": "Meetup record not found"
        }, 404

parser.add_argument("status", help="This field cannot be blank")
mod_rsvp = meetups.model("RSVP to a meetup", {
    "status": fields.String("Must be a Yes, No or Maybe")
})


@meetups.route("/<meetup_id>/rsvps")
class RsvpToMeetup(Resource):
    @meetups.doc(security="apikey")
    @meetups.expect(mod_rsvp)

    def post(self, meetup_id):
        args = parser.parse_args()
        status = args["status"]

        status = status.lower()

        if (status != "yes" and status != "no" and status != "maybe"):
            return {"error": "Status should be a Yes, No or Maybe"}

        meetup = meetup_model.Meetups.get_specific_meetup(meetup_id)
        if meetup:
            return {
                "status": 201,
                "data": [{
                    "meetup": meetup_id,
                    "status": status
                }]
            }, 201

        


