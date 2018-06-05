Feature: Web words analyzer
    In order to see how many words are typing by day
    As users
    We'll implement a web that will use a url to get text and save it in a data base


    Scenario: Analyze a normal url
      Given I have the text "http://127.0.0.1:8000/"
      When I put it in the url textfield
      And I click the execute button
      Then I see that text in the result text
            """
          ver 1
guarro 1
esto 1
carajo 1
se 1
      """
      And I see in the url textfield the text ""
      And I see in the date textfield the text ""

    Scenario: Invalid url
      Given I have the text "invalidUrl"
      When I put it in the url textfield
      And I click the execute button
      Then I see that text in the result text
    """
    No se ha podido leer la pagina
    """
      And I see in the url textfield the text ""
      And I see in the date textfield the text ""

    Scenario: Invalid date
      Given I have the text "invalidDate"
      When I put it in the date textfield
      And I click the seeDate button
      Then I see that text in the result text
    """
    """
      And I see in the url textfield the text ""
      And I see in the date textfield the text ""

    Scenario: Analyze a normal date
      Given I have the text "testDate"
      When I put it in the date textfield
      And I click the seeDate button
      Then I see that text in the result text
            """
          guarro 5.0
muy 4.0
es 3.0
tambien 2.0
esto 1.0
      """
      And I see in the url textfield the text ""
      And I see in the date textfield the text ""

    Scenario: With 2 textfield not empty, and click execute, both are empty
      Given I have the text "Lo que sea"
      When I put it in the date textfield
      And I put it in the url textfield
      And I click the execute button
      Then I see in the url textfield the text ""
      And I see in the date textfield the text ""


    Scenario: With 2 textfield not empty, and click seeDate, both are empty
      Given I have the text "Lo que sea"
      When I put it in the date textfield
      And I put it in the url textfield
      And I click the seeDate button
      Then I see in the url textfield the text ""
      And I see in the date textfield the text ""
