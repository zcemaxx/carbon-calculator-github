# Carbon Calculator

cement_type = input("Enter the cement type: ")

# a general formula for either fossil fuel emission or electricity energy mix emission
def combustion_emission (fuel, emission_factor)
    return

def power_emission(energy_mix, emission_energy_mix):
    return energy_mix * emission_energy_mix

# A1 emission: CO2 emission from raw material supply
def a1_emission(extraction, explosives, crushing):
    return extraction + explosives + crushing

# Calculate limestone required for 1 tonne cement
cement_unit_mass = 1  # (unit in tonne)
clinker_in_cement = float(input("Enter the clinker in cement (%): "))
# clinker components wt. % vary case by case (value inputs here) #
clinker_components = {"tricalcium silicate 3CaO.SiO2": 50, "dicalcium silicate 2CaO.SiO2": 25,
                      "tricalcium aluminate 3CaO.Al2O3": 10, "tetracalcium alumniorferrite 3CaO.Al2O3.Fe2O3": 10,
                      "Gypsum": 5
                      }  # (unit %)
CaO_in_clinker = float((clinker_components["tricalcium silicate 3CaO.SiO2"] * (56*3/228)) +
                       (clinker_components["dicalcium silicate 2CaO.SiO2"] * (56*2/172)) +
                       (clinker_components["tricalcium aluminate 3CaO.Al2O3"] * (56*3/270)) +
                       (clinker_components["tetracalcium alumniorferrite 3CaO.Al2O3.Fe2O3"] * (56*3/429.64))
                       )
print("CaO weights in clinker {:.2%}.". format(CaO_in_clinker/100))
CaCO3_CaO_ratio = 1.785  # (stoichiometric ratio, as 100/56)
CaCO3_required = cement_unit_mass * clinker_in_cement/100 * CaO_in_clinker/100 * CaCO3_CaO_ratio # unit in tonne
mineral_purity = float(input("Enter the mineral purity (%): "))
limestone_required = float(CaCO3_required / (mineral_purity/100))
print("Limestone required to produce 1 tonne cement: {:.2f} tonne.". format(limestone_required))

# Calculate energy consumed to run crusher for 1 tonne cement
crusher_capacity = float(input("Enter the crusher capacity (t/hr): "))
time_crushing_1_tonne = float(1/crusher_capacity)  # (unit in hrs)
crusher_power = float(input("Enter the crusher power (KW): "))
energy_crushing_1_tonne = time_crushing_1_tonne * crusher_power  # (unit in KWh)
total_energy_crushing = limestone_required * energy_crushing_1_tonne
print("Total energy to crush limestone per 1 tonne cement produced: {:.3f} KWh.".format(total_energy_crushing))

# Calculate CO2 emission for crushing limestone per 1 tonne cement produced
# UK grid mix # CO2 emission from energy mix # (value inputs here)
# Source: https://www.gov.uk/government/publications/fuel-mix-disclosure-data-table/fuel-mix-disclosure-data-table#fn:1 #
UK_grid_mix = {"Coal": 6.3,
               "Natural Gas": 35,
               "Nuclear": 12.7,
               "Renewables": 43.2,
               "other": 2.8
               }  # (unit %)
CO2_emission_from_energy_mix = {"Coal": 1.046,
                                "Natural Gas": 0.375,
                                "Nuclear": 0,
                                "Renewables": 0,
                                "other": 0.877
                                } # (unit in kg CO2eq./KWh)
# Average CO2 emission from UK grid mix = Grid mix × CO2 emission from energy mix
average_CO2_emission_UK_grid_mix = sum((UK_grid_mix[key]/100) * CO2_emission_from_energy_mix[key] for key in UK_grid_mix)  # CO2 emission per 1KWh energy
print("Average CO2 emission from UK grid mix: {:.5f} kg CO2eq./KWh.".format(average_CO2_emission_UK_grid_mix))
# Calculate CO2 emission from crushing limestone
CO2_emission_crushing_limestone = average_CO2_emission_UK_grid_mix * total_energy_crushing
print("CO2 emission from crushing limestone per 1 tonne cement produced: {:.2f} kg CO2eq.".format(CO2_emission_crushing_limestone))

# CO2 emission from transport
# Limestone required / Truck loading capacity × Fuel consumption per truck per km × Transporting distance × CO2 emission per 1L diesel
# Truck loading capacity varies case by case (value inputs here) #
truck_loading = 18  # (unit in tonne)
fUel_consumption_per_truck_100km = 30 # unit in l/100km
# Transportation distance from quarrying site to processing unit
distance = 50 # unit in km
CO2_emission_diesel = 3 # unit in kg/l
# Calculate the CO2 emission from transportation
CO2_emission_transport = float (limestone_required / truck_loading * (fUel_consumption_per_truck_100km / 100) * distance * CO2_emission_diesel)
print("CO2 emission from transporting limestone per 1 tonne cement produced: {:.2f} kg CO2eq.". format(CO2_emission_transport))

# Explosives emission
# Amount of explosive used per 1 tonne limestone extracted × Limestone required for 1 ton cement × Emission factor of explosive
explosives_amount = float(input("Enter amount of explosives used per 1 tonne limestone extracted (kg): "))
emission_factor_explosives = 0.1
CO2_emission_explosives = float(explosives_amount * limestone_required * emission_factor_explosives)
print("CO2 emission from explosives per 1 tonne cement produced: {:.2f} kg CO2eq.".format(CO2_emission_explosives))

A1_emission = a1_emission(CO2_emission_transport,CO2_emission_explosives,CO2_emission_crushing_limestone)
print("A1 emission, CO2 from raw material supply per 1 tonne cement produced: {:.2f} kg CO2eq.".format(A1_emission))


def a2_emission (transport)
    return transport

def a3_emission (roller_mill_blender, CO2_process, fuel_combustion, cooling_fan, conveyor)
    return roller_mill_blender + CO2_process + fuel_combustion + cooling_fan + conveyor

# Roller mill blender operation
# Time per blending 1 ton raw materials × raw materials required for 1 ton cement × Energy consumed to run roller mill blender × CO2 emission per 1KWh energy


# CO2/CaCO3 Stoichiometric Ratio
CO2_CaCO3_ratio = 0.44
CO2_chemical = CO2_CaCO3_ratio * CaCO3_required * 1000
print("CO2 emission in chemical reaction to produce 1 tonne cement: {:.2f} kg.". format(CO2_chemical))

def carbon_calculator(A1_emission, A2_emission, A3_emission):
    return A1_emission + A2_emission + A3_emission
print("{} produces .". format(cement_type))

