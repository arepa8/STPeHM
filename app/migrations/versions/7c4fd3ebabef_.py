"""empty message

Revision ID: 7c4fd3ebabef
Revises: None
Create Date: 2016-06-30 22:39:15.989792

"""

# revision identifiers, used by Alembic.
revision = '7c4fd3ebabef'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Institution',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('address', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('address'),
    sa.UniqueConstraint('name')
    )
    op.create_table('Role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('role_name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('role_name')
    )
    op.create_table('Specialization',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('speciality', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('speciality')
    )
    op.create_table('InstitutionElement',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('institution_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['institution_id'], ['Institution.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('User',
    sa.Column('ci', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=16), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('role', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['role'], ['Role.id'], ),
    sa.PrimaryKeyConstraint('ci'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('Appointment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('patient', sa.Integer(), nullable=False),
    sa.Column('doctor', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=False),
    sa.ForeignKeyConstraint(['doctor'], ['User.ci'], ),
    sa.ForeignKeyConstraint(['patient'], ['User.ci'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('DoctorAbilities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ci_user', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=500), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['ci_user'], ['User.ci'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('DoctorAwards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ci_user', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=500), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('institution', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['ci_user'], ['User.ci'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('DoctorEvents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ci_user', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=500), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('institution', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['ci_user'], ['User.ci'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('DoctorExperiences',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ci_user', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=500), nullable=True),
    sa.Column('date_of_start', sa.Date(), nullable=True),
    sa.Column('date_of_finish', sa.Date(), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('institution', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['ci_user'], ['User.ci'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('DoctorProfile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ci_user', sa.Integer(), nullable=False),
    sa.Column('sex', sa.String(length=10), nullable=True),
    sa.Column('date_of_birth', sa.Date(), nullable=True),
    sa.Column('marital_status', sa.String(length=15), nullable=True),
    sa.Column('telephone', sa.String(length=15), nullable=True),
    sa.Column('address', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['ci_user'], ['User.ci'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('DoctorPublications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ci_user', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('authors', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('magazine', sa.String(length=100), nullable=True),
    sa.Column('number', sa.String(length=5), nullable=True),
    sa.Column('volume', sa.String(length=5), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['ci_user'], ['User.ci'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('DoctorStudies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ci_user', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=500), nullable=True),
    sa.Column('date_of_graduation', sa.Date(), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('institution', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['ci_user'], ['User.ci'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Doctor_Specialization',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('doctor', sa.Integer(), nullable=False),
    sa.Column('speciality', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['doctor'], ['User.ci'], ),
    sa.ForeignKeyConstraint(['speciality'], ['Specialization.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('FamilyBackground',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ci_user', sa.Integer(), nullable=False),
    sa.Column('asthma', sa.Boolean(), nullable=True),
    sa.Column('cancer', sa.Boolean(), nullable=True),
    sa.Column('heartdisease', sa.Boolean(), nullable=True),
    sa.Column('diabetes', sa.Boolean(), nullable=True),
    sa.Column('liverdisease', sa.Boolean(), nullable=True),
    sa.Column('hypertension', sa.Boolean(), nullable=True),
    sa.Column('other', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['ci_user'], ['User.ci'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('NonPathologicalBackground',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ci_user', sa.Integer(), nullable=False),
    sa.Column('defecation', sa.String(length=100), nullable=True),
    sa.Column('toothbrushing', sa.String(length=100), nullable=True),
    sa.Column('cigarrettes', sa.String(length=100), nullable=True),
    sa.Column('years', sa.String(length=100), nullable=True),
    sa.Column('beverages', sa.String(length=100), nullable=True),
    sa.Column('frecuency', sa.String(length=100), nullable=True),
    sa.Column('physical_activity', sa.String(length=500), nullable=True),
    sa.Column('frecuency2', sa.String(length=100), nullable=True),
    sa.Column('other', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['ci_user'], ['User.ci'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('PathologicalBackground',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ci_user', sa.Integer(), nullable=False),
    sa.Column('current_condition', sa.String(length=500), nullable=True),
    sa.Column('surgical_history', sa.String(length=500), nullable=True),
    sa.Column('transfusional_history', sa.String(length=500), nullable=True),
    sa.Column('allergies', sa.String(length=500), nullable=True),
    sa.Column('traumatic_history', sa.String(length=500), nullable=True),
    sa.Column('hospitalizations', sa.String(length=500), nullable=True),
    sa.Column('addictions', sa.String(length=500), nullable=True),
    sa.Column('other', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['ci_user'], ['User.ci'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('PatientConsultation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ci_patient', sa.Integer(), nullable=False),
    sa.Column('ci_doctor', sa.Integer(), nullable=False),
    sa.Column('name_doctor', sa.String(length=500), nullable=True),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('motive', sa.String(length=500), nullable=True),
    sa.Column('symptoms', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['ci_doctor'], ['User.ci'], ),
    sa.ForeignKeyConstraint(['ci_patient'], ['User.ci'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('PatientProfile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ci_user', sa.Integer(), nullable=False),
    sa.Column('sex', sa.String(length=10), nullable=True),
    sa.Column('date_of_birth', sa.Date(), nullable=True),
    sa.Column('marital_status', sa.String(length=15), nullable=True),
    sa.Column('telephone', sa.String(length=15), nullable=True),
    sa.Column('address', sa.String(length=100), nullable=True),
    sa.Column('heigth', sa.String(length=15), nullable=True),
    sa.Column('weigth', sa.String(length=15), nullable=True),
    sa.Column('blood_type', sa.String(length=2), nullable=True),
    sa.Column('diabetic', sa.String(length=1), nullable=True),
    sa.Column('allergies', sa.String(length=500), nullable=True),
    sa.Column('emergency_contact', sa.String(length=100), nullable=True),
    sa.Column('emergency_number', sa.String(length=15), nullable=True),
    sa.Column('comments', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['ci_user'], ['User.ci'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('PatientProfile')
    op.drop_table('PatientConsultation')
    op.drop_table('PathologicalBackground')
    op.drop_table('NonPathologicalBackground')
    op.drop_table('FamilyBackground')
    op.drop_table('Doctor_Specialization')
    op.drop_table('DoctorStudies')
    op.drop_table('DoctorPublications')
    op.drop_table('DoctorProfile')
    op.drop_table('DoctorExperiences')
    op.drop_table('DoctorEvents')
    op.drop_table('DoctorAwards')
    op.drop_table('DoctorAbilities')
    op.drop_table('Appointment')
    op.drop_table('User')
    op.drop_table('InstitutionElement')
    op.drop_table('Specialization')
    op.drop_table('Role')
    op.drop_table('Institution')
    ### end Alembic commands ###
