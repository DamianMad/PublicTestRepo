# Single Bet Placement Feature - Test Plan

## Important information

Before executing any test, you need to have valid user that will authorize you to execute below tests!

## Objective

The purpose of this test plan is to validate the most critical risks of the **Single Bet Placement** feature, with focus on:
- successful bet creation,
- stake validation,
- balance handling

---

## Test Scenarios

### TC-01 Successful single bet placement
**Priority:** Critical

**Type:** Automated  

**Risk Rationale:**  
This is the core business flow of the feature. If a valid single bet cannot be placed, or if the wallet balance is updated incorrectly, the feature fails at both revenue and user trust levels.

**Steps:**
1. Open the betting page for an available football match
2. Select one valid betting outcome
3. Enter stake value `10.09`
4. Submit the single bet

**Expected Result:**
- Loading state appear ('Placing...')
- Bet is accepted successfully
- Bet summary appear with correct data
- User balance is reduced by exactly `10.09`

---

### TC-02 Bet that exceeds available balance
**Priority:** Critical  

**Type:** Automated  

**Risk Rationale:**  
Allowing a user to place a bet above available balance breaks a core financial rule and may lead to invalid transactions, incorrect wallet state, and loss of trust.

**Steps:**
1. Open the betting page for an available virtual match
2. Select one valid betting outcome
3. Enter stake value greater than the available balance

**Expected Result:**
- Place bet button should be greyed and unavailable
- 'Insufficient balance' error appear under state 
- No bet is created
- User balance remains unchanged

---

### TC-03 Stake boundary validation for minimum and maximum allowed amount
**Priority:** High 

**Type:** Manual  

**Risk Rationale:**  
Boundary values are common sources of validation defects. Incorrect handling of minimum or maximum stake may allow invalid bets or block valid ones.

**Steps:**
1. Open the betting page for an available virtual match
2. Select one valid betting outcome
3. Enter a stake below 1 EUR (+decimals scenario)
4. Enter a stake equal 1 EUR (+decimals scenario)
5. Enter a stake equal 100 EUR (+decimals scenario)
6. Enter a stake above 100 EUR (+decimals scenario)

**Expected Result:**
- Stake below minimum is rejected with error Minimum stake is €1.00 visible under stake
- Stake equal to minimum is accepted
- Stake equal to maximum is accepted
- Stake above maximum is rejected with error Maximum stake is €100.00 visible under stake

---

### TC-04 Balance remains unchanged when bet placement fails
**Priority:** High

**Execution:** Manual  

**Risk Rationale:**  
Failed bet placement must not affect user funds. If the balance is reduced despite the bet being rejected, it creates a critical financial inconsistency, directly impacts user trust, and may indicate missing transactional integrity between bet validation and wallet update.

**Steps:**
1. Open the betting page for an available virtual match
2. Select one valid betting outcome
3. Enter each invalid stake value one by one
4. Attempt to submit the bet for each input

**Expected Result:**
- Each invalid stake is rejected
- Relevant validation message is shown for invalid input
- No bet is created
- User balance remains unchanged
- The system remains stable and responsive

---

### TC-05 Replacment and deletion of bet
**Priority:** High 

**Execution:** Manual  

**Risk Rationale:**  
This scenario verifies that bet slip actions correctly update the current selection state before confirmation. Additionaly it check if we are able to delete bet by interact with correct buttons.

**Steps:**
1. Open the betting page for an available virtual match
2. Pick any available match
3. Choose random prediciton
4. Pick any different available match
5. Delete it by clicking on 'Ramove all' button on bet slip section
6. Add it once again
7. Delete it by click on 'x' button on bet slip section

**Expected Result:**
- You should see only one bet at all the time
- All exist bet should be replaced by choosing different match
- Deletion should be completed after clicking on 'Remove all' or 'x' button 

---

### TC-06 Date and odds filtering
**Priority:** Low 

**Execution:** Manual  

**Risk Rationale:**  
This scenario verifies that filtering features works as expected and if visible data is correct according to choosen settings.

**Steps:**
1. Open the betting page for an available virtual match
2. Choose the single Date and check outcome
3. Choose any range of Date and check outcome
4. Manipulate Odds range and check outcome
5. Reset Odds
6. Reset Date

**Expected Result:**
- Outcome should always match to provided date or odds in filtering
- Reset process should bring back default setting of Date or Odds (default Date is today, default Odds range is 1-10)
- Deletion should be completed after clicking on 'Remove all' or 'x' button
- Selected data should be displayed in right upper corner of filtering window

## Automation Scope
The following scenarios are selected for automation:
- **TC-01 Successful single bet placement**
- **TC-02 Bet that exceeds available balance**

These two tests provide the strongest value in limited time because they validate:
- the primary happy path,
- a critical business rule,
- wallet balance integrity,
- core API/UI behavior.

## Out of Scope
Due to time constraints, lower-risk exploratory areas such as advanced filtering, layout/visual checks, and broader compatibility testing are not included in this initial set.