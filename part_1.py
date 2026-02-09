def main():
#list
    sample_bay = ["Basalt","Silica","Iron","Dust"]
    new_findings = []

    print("\n---initialising---")
    print("------------------")
    print("Collected Samples")
    print("------------------")
#1.1
    def storage_bay():
        print(f"first Item: " + str(sample_bay[0]))
        print(f"Last Item: " + str(sample_bay[-1]))
        print(f"Total Items: " + str(len(sample_bay)))

    storage_bay()
    
    print("------------------")
#1.2
    def analysing_samples():
        for sample in sample_bay:
            print(f"Transmitting data for: " + sample)

    analysing_samples()
        
    print("\nData transmitted")
    print("------------------")
#1.3
    def collection(): 
        for _ in range(3):
            new_sample = input("Enter New sample: ").title()
            new_findings.append(new_sample)
    
    collection()

    print(f"New collected samples: " + str(new_findings))
    print("New findings recorded")
    print("------------------")
#1.4
    def Jettison(): 
        if "Dust" in sample_bay:
            sample_bay.remove("Dust")
            print("Dust removed")
        else:
            print("No dust found")

    Jettison()
    
main()