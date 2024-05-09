from unittest.mock import patch
import os

import pytest

from src.settings import (
    Env, 
    ApplicationSettings, 
    DatabaseSettings, 
    GeneralSettings, 
    get_settings,
    execution_environment
)
from tests.resouces import settings as settings_mock


@pytest.mark.parametrize(
    argnames='attr, value', 
    argvalues=[
        ('PRD', 'prd'),
        ('STG', 'stg'),
        ('HML', 'hml'),
        ('DEV', 'dev'),
        ('UNITTEST', 'unittest')
    ]
)
def test_environemt_enum_as_string(attr, value):
    # arrange
    # act
    # assert
    assert Env.__members__.get(attr) == value


@pytest.mark.parametrize(
    argnames='attr, match', 
    argvalues=[
        (Env.PRD,      False),
        (Env.UNITTEST, True)
    ]
)
def test_execution_environment_then_return_bool(attr, match):
    # arrange
    # act
    # assert
    assert execution_environment(attr) is match


def test_application_settings_with_environment_variables_mock():
    # arrange
    with patch.dict(os.environ, settings_mock.APPLICATION_SETTINGS_ENVIRONMENT_VARIABLES):
        # act
        appliaction_settings = ApplicationSettings()
    # assert
    assert appliaction_settings.application_name == 'tst-name'
    assert appliaction_settings.application_host == '0.0.0.0'
    assert appliaction_settings.application_port == 1234
    assert appliaction_settings.environment == 'dev'
    assert appliaction_settings.workers == 1
    assert appliaction_settings.timeout_graceful_shutdown == 5


def test_database_settings_with_environment_variables_mock():
    # arrange
    with patch.dict(os.environ, settings_mock.DATABASE_SETTINGS_ENVIRONMENT_VARIABLES):
        # act
        database_settings = DatabaseSettings()
    # assert
    assert database_settings.database_username == 'postgres'
    assert database_settings.database_password == 'postgres'
    assert database_settings.database_host == 'localhost'
    assert database_settings.database_port == 5432
    assert database_settings.database_name == 'postgres'
    assert database_settings.unittest_sync_uri == 'sqlite:///unittest.db'


def test_general_settings_embeded_config_class():
    # arrange
    with patch.dict(
        os.environ, 
        settings_mock.APPLICATION_SETTINGS_ENVIRONMENT_VARIABLES, 
        settings_mock.DATABASE_SETTINGS_ENVIRONMENT_VARIABLES
    ):
        # act
        general_settings = GeneralSettings
    # assert
    assert isinstance(general_settings.application_settings, ApplicationSettings)
    assert isinstance(general_settings.database_settings, DatabaseSettings)


def test_get_settings_then_return_general_settings():
    # arrange
    # act
    # assert
    assert isinstance(get_settings(), GeneralSettings)


def test_get_settings_cache_then_return_same_object():
    # arrange
    settings_one = get_settings()
    settings_two = get_settings()
    # act
    # assert
    settings_one is settings_two
