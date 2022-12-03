import pytest
from selene.support.shared import browser
from selene import be, have, by, command
import time
import os


def test_open():
    browser.open("automation-practice-form")
    browser.element("#firstName").type("John")
    browser.element("#lastName").type("Doe")
    browser.element("#userEmail").type("JohnDoe@gmail.com")
    browser.element("[for='gender-radio-1']").click()
    browser.element("#userNumber").type("78674563423")
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__year-select").click()
    browser.element("[value='1992']").click()
    browser.element(".react-datepicker__month-select").click()
    browser.element("[value='7']").click()
    browser.element(".react-datepicker__day.react-datepicker__day--018").click()
    browser.element("#subjectsInput").type("Eng").press_enter()
    browser.element('#hobbies-checkbox-2').perform(command.js.scroll_into_view)
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + "/download.jpeg")
    browser.element('#currentAddress').type("Earth_planet")
    browser.all("[id^=google_ads_iframe]").perform(command.js.remove)
    browser.element('#state').click()
    browser.element('#react-select-3-option-0').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()
    browser.element("#submit").press_enter()
    browser.all('.table-responsive td:nth-child(2)').should(have.texts("John Doe",
                                                                       "JohnDoe@gmail.com",
                                                                       "Male",
                                                                       '7867456342',
                                                                       "18 August,1992",
                                                                       "English",
                                                                       "Reading",
                                                                       "download.jpeg",
                                                                       "Earth_planet",
                                                                       "NCR Delhi"
                                                                       ))
