*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***         StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
Move in middle of board    5             5             0                     EAST          6           5           1
Move in middle of board    5             5             1                     WEST          4           5           2
Move in middle of board    5             5             1                     NORTH         5           4           2
Move in middle of board    5             5             1                     SOUTH         5           6           2
Move on t-l of board       0             0             0                     WEST          0           0           1
Move on t-l of board       0             0             0                     EAST          1           0           1
Move on t-l of board       0             0             0                     NORTH         0           0           1
Move on t-l of board       0             0             0                     SOUTH         0           1           1
Move on b-r of board       9             9             0                     EAST          9           9           1
Move on b-r of board       9             9             0                     WEST          8           9           1
Move on b-r of board       9             9             0                     NORTH         9           8           1
Move on b-r of board       9             9             0                     SOUTH         9           9           1


*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}
