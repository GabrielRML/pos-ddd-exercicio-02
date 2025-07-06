from flask import Blueprint, request, jsonify
from application.use_cases.create_participant import CreateParticipantUseCase
from application.use_cases.list_participants import ListParticipantsUseCase
from application.use_cases.delete_participant import DeleteParticipantUseCase
from infrastructure.repositories.participant_repository_impl import ParticipantRepositoryImpl
from infrastructure.database.connection import SessionLocal

participant_bp = Blueprint('participant', __name__)

session = SessionLocal()
participant_repository = ParticipantRepositoryImpl(session)
create_participant_use_case = CreateParticipantUseCase(participant_repository)
list_participants_use_case = ListParticipantsUseCase(participant_repository)
delete_participant_use_case = DeleteParticipantUseCase(participant_repository)

@participant_bp.route('/participants', methods=['POST'])
def create_participant():
    data = request.json
    create_participant_use_case.execute(data['name'], data['email'])
    return jsonify({"message": "Participant created successfully"}), 201

@participant_bp.route('/participants', methods=['GET'])
def list_participants():
    participants = list_participants_use_case.execute()
    return jsonify([participant.__dict__ for participant in participants])

@participant_bp.route('/participants/<int:participant_id>', methods=['DELETE'])
def delete_participant(participant_id):
    delete_participant_use_case.execute(participant_id)
    return jsonify({"message": "Participant deleted successfully"})
