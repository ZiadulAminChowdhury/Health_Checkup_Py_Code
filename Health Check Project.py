def calculate_bmi(weight, height, weight_unit, height_unit):
    if weight_unit == 'lbs':
        weight = weight * 0.453592
    if height_unit == 'inches':
        height = height * 0.0254
    elif height_unit == 'feet':
        height = height * 0.3048
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return bmi, category

def categorize_blood_pressure(systolic, diastolic, age):
    if systolic < 121 and diastolic < 81:
        category = "Normal"
    elif 121 <= systolic < 130 and diastolic < 81:
      category = "Elevated"
    elif 130 <= systolic < 140 or 80 <= diastolic < 90:
      category = "Stage 1 Hypertension"
    elif systolic >= 140 or diastolic >= 90:
      category = "Stage 2 Hypertension"
    else:
      category = "Hypertensive Crisis"
    return category


def categorize_diabetes(value, unit, test_type):
    if unit == 'mmol/l':
        if test_type == 'f':
            if value < 5.6:
                category = "Normal"
            elif 5.6 <= value <= 6.9:
                category = "Prediabetes"
            else:
                category = "Diabetes"
        elif test_type == 'r':
            if value < 7.8:
                category = 'Normal'
            elif 7.8 <= value <= 11.0:
                category = "Prediabetes"
            else:
                category = "Diabetes"
        else:
            category = "Invalid test type"
    elif unit == 'mg/dl':
        if test_type == 'f':
          if value < 100:
              category = "Normal"
          elif 100 <= value <= 125:
              category = "Prediabetes"
          else:
              category = "Diabetes"
        elif test_type == 'r':
            if value < 140:
                category = "Normal"
            elif 140 <= value <= 199:
                category = "Prediabetes"
            else:
                category = "Diabetes"
        else:
            category = "Invalid test type"
    else:
        category = "Invalid unit"
    return category


while True:
    print("\nHealth Check Options:")
    print("1. BMI Calculator")
    print("2. Blood Pressure Check")
    print("3. Diabetes Check")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        weight_unit = input("Enter weight unit (kg or lbs): ").lower()
        weight = float(input("Enter your weight: "))
        height_unit = input("Enter height unit (meters or inches): ").lower()
        height = float(input("Enter your height: "))
        bmi, category = calculate_bmi(weight, height, weight_unit, height_unit)
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")
    elif choice == '2':
        age = int(input("Enter your age: "))
        systolic = int(input("Enter your systolic blood pressure: "))
        diastolic = int(input("Enter your diastolic blood pressure: "))
        category = categorize_blood_pressure(systolic, diastolic, age)
        print(f"Your blood pressure category: {category}")
    elif choice == '3':
        value = float(input("Enter your blood glucose value: "))
        unit = input("Enter the unit (mmol/l or mg/dl): ").lower()
        test_type = input("Enter the test type (f for fasting or r for random): ").lower()
        category = categorize_diabetes(value, unit, test_type)
        print(f"Your diabetes category: {category}")
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
