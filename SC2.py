#Name:Misa
#Class: 6th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be told their BMI as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

height=float(input("What is your height?"))
weight=float(input("What is your weight?"))
print(height,weight)


#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right

if height>5.1 and weight<114.4:
    print("BMI is less that 18.5! You are underweight")

elif height==5.5 and weight>114.4 or weight<154.5:
    print("BMI is 18.5 to24.9! You are a healthy weight")

elif height<5.6 and weight>154.6 or weight<185.5:
    print("BMI is 25 to 29.9. You are over weight")

elif height<5.6 and weight>185.5:
    print("BMI is 30 or more. You are obese")
