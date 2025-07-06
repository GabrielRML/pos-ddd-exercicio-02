from flask import Blueprint, request, jsonify
from application.use_cases.create_event import CreateEventUseCase
from application.use_cases.list_events import ListEventsUseCase
from application.use_cases.delete_event import DeleteEventUseCase
from infrastructure.repositories.event_repository_impl import EventRepositoryImpl
from infrastructure.database.connection import SessionLocal

event_bp = Blueprint('event', __name__)

session = SessionLocal()
event_repository = EventRepositoryImpl(session)
create_event_use_case = CreateEventUseCase(event_repository)
list_events_use_case = ListEventsUseCase(event_repository)
delete_event_use_case = DeleteEventUseCase(event_repository)

@event_bp.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    create_event_use_case.execute(data['name'], data['description'], data['date'])
    return jsonify({"message": "Event created successfully"}), 201

@event_bp.route('/events', methods=['GET'])
def list_events():
    events = list_events_use_case.execute()
    return jsonify([event.__dict__ for event in events])

@event_bp.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    delete_event_use_case.execute(event_id)
    return jsonify({"message": "Event deleted successfully"})
