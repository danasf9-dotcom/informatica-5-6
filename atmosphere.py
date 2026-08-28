def main():
   layer = input("Descent Atmosphere layer: ").strip().lower()

   if layer == "Exsophere":
      print("Your altitude level will between 700 and 10,000 km.")
   elif layer == "Thermosphere":
        print("Your altitude level will between 85 and 700 km.")
   elif layer == "Mesosphere":
        print("Your altitude level will between 50 and 85 km.")
   elif layer == "Stratosphere":
        print("Your altitude level will between 12 and50 km.")
   elif layer == "Troposphere":
        print("Your altitude level will between 0 and 12 km.")
   else :
       print("Inexistent layer.")

   altitude = float(input("Enter exact altitude: "))
   time = 0
   if altitude > 700:
       time += (altitude - 700) / 2
       altitude = 700
   if altitude > 85:
       time += (altitude - 85) / 0.5
       altitude = 85
   if altitude += > 50:
      time += (altitude - 50) / 0.2
      altitude = 50
   if altitude > 12:
      time += (altitude - 12) / 0.075
      altitude = 12

      time += altitude / 0.02
      print("Total time:, round(time, 1))

if __name__ == "__main__":
     main()








if __name__ == "__main__":
   main()
