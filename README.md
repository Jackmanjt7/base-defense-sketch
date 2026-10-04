
User: Most likely a logistician preparing a local base defense sketch
Input: Assets available
Output: Ideal base defense sketch with gun positions, and recommended distances based off doctrine from various points.
Success Condition: A user can create two assets, position them, see their distance, save, and reload. 


Nouns in this project:
Scenario: name, units, grid scale, perimeter.
	EX: FSC, (5xM2, 2x HIPPO, 4x M978s) ,1:100m, (calculated)
Asset: ID, display name, category, quantity, position
	EX: M2-0001, M2 Machine Gun, Weaponsystem, x1, (position)
Position: x-coord, y-coord
	EX: 1,2
SeparationRule: source category, target category, minimum distance
	EX: CL I Water, CL III Fuel, 500 meters
DistanceResult: two asset IDs, measured distance, rule status
	EX: (HIPPO-0001, FUELER-0001), 501 m, true
