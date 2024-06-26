default_initial_settings = {
    "name": "Goofoo Near",
    "manufacturer": "GooFoo",
    "start_gcode": "G28 ;Home\nG1 Z15.0 F6000 ;Move the platform down 15mm\n;Prime the extruder\nG92 E0\nG1 F200 E3\nG92 E0",
    "end_gcode": "G91 ;Relative positioning\nG1 E-2 F2700 ;Retract the filament\nG1 E-2 Z0.2 F2400 ;Retract and raise Z\nG1 X5 Y5 F3000 ;Wipe out\nG1 Z10 ;Raise Z more\nG90 ;Absolute positioning\n\nG28 X0 Y0 ;Home X and Y\n\nM106 S0 ;Turn-off fan\nM104 S0 ;Turn-off hotend\nM140 S0 ;Turn-off bed\n\nM84 X Y E ;Disable all steppers but Z",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 40.0,
    "travel_speed": 80,
    "dia_feed": 1.75,
    "build_volume_x": 100,
    "build_volume_y": 100,
    "build_volume_z": 100,
}
