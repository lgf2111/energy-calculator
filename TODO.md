Frontend
- Home Page
    - Statistics, Graphs
- Calculator
    - Efficiency Level options should show ticks not numbers
    - "Add" button
    - "Calculate" button
    - Css Animation for add and calculate
    - When using washing machine hours used shld be times used per day
        - Can just assume 1h = 1times per day, need to just state it if user chooses washing machine as appliance
    - Script to filter brand name for every appliance
    - form shld be col-10, current width too small
    - when adding, another CalculatorForm is used
- Result
    - container div split to half, left is calculated result, right is what can be done to save energy/money
- Admin
    - No reco fn

Backend
- Home Page
    - Produce statistics, graph
        - Just copy paste wtv relevant data could be found, dn dynamic
        - If possible find api to get data
    - Admin page view fix
- Calculator
    - If form submit valid:
        - use for loop to iterate with the amount of appliances added
        - use calculate algo, get result
        - redirect to Result
- Result
    - with calculated result, use recommend algo to get recommendation