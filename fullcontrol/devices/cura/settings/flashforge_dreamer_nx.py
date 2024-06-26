default_initial_settings = {
    "name": "Dreamer NX",
    "manufacturer": "Flashforge",
    "start_gcode": ";Start Gcode\nG90 ;absolute positioning\nM118 X25.00 Y25.00 Z20.00 T0\nM140 S{data['bed_temp']} T0 ;Heat bed up to first layer temperature\nM104 S{data['nozzle_temp']} T0 ;Set nozzle temperature to first layer temperature\nM107 ;start with the fan off\nG90\nG28\nM132 X Y Z A B\nG1 Z50.000 F420\nG161 X Y F3300\nM7 T0\nM6 T0\nM651\nM907 X100 Y100 Z40 A100 B20 ;Digital potentiometer value\nM108 T0\n;Purge line\nG1 X-110.00 Y-60.00 F4800\nG1 Z{0.1} F420\nG1 X-110.00 Y60.00 E17,4 F1200\n;Purge line end",
    "end_gcode": ";end gcode\nM104 S0 T0\nM140 S0 T0\nG162 Z F1800\nG28 X Y\nM652\nM132 X Y Z A B\nG91\nM18",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 120,
    "dia_feed": 2.85,
    "build_volume_x": 230,
    "build_volume_y": 150,
    "build_volume_z": 140,
}
