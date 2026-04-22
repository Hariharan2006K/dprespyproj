import streamlit as st

st.markdown("<h1 class='main-header'>Survival Guides</h1>", unsafe_allow_html=True)
st.caption("Review scientific backgrounds and explicit operational directives for different regional hazards.")

st.markdown("---")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🏚️ Earthquakes", 
    "🛶 Floods", 
    "🧯 Fires", 
    "🌬️ Cyclones", 
    "🏜️ Heatwaves"
])

with tab1:
    st.markdown("## 🏚️ Earthquakes")
    
    st.subheader("Geological Context")
    st.write("""
    Earthquakes are the result of sudden movement along faults within the Earth's crust. The movement releases stored-up 'elastic strain' energy in the form of seismic waves, which propagate through the Earth and cause the ground surface to shake. 
    - **Tectonic Plates:** The Earth's crust consists of multiple massive plates that constantly collide, pull apart, or scrape against each other.
    - **Measurement:** Earthquakes are measured using seismographs. The Magnitude (like the Moment Magnitude Scale) measures the energy released, while the Mercalli intensity scale measures the observed effects.
    """)
    
    st.subheader("Operational Directives")
    st.markdown("""
    #### 1. Mitigation & Preparedness (Before)
    - **Home Retrofitting:** Bolt heavy furniture (e.g., bookcases, water heaters) to the wall studs to prevent them from toppling.
    - **Identify Safe Spots:** Find sturdy tables or desks in each room to take cover under.
    - **Build a Kit:** Maintain a 72-hour emergency kit including water (1 gallon per person per day), non-perishable food, a whistle, a flashlight, and a first-aid kit.
    
    #### 2. Immediate Action (During)
    - **Indoors:** **Drop, Cover, and Hold On**. Drop to your hands and knees. Cover your head and neck (and your entire body if possible) under a sturdy table. Hold on to your shelter until the shaking stops. *Do not use doorways.*
    - **Outdoors:** Move away from buildings, streetlights, and utility wires.
    - **In a Vehicle:** Stop as quickly as safety permits and stay in the vehicle. Avoid stopping near or under buildings, trees, overpasses, and utility wires.
    
    #### 3. Recovery Phase (After)
    - **Beware of Aftershocks:** These secondary shockwaves can happen for hours, days, or months after the main quake.
    - **Check Utilities:** Sniff for gas leaks. If you smell gas or hear a blowing/hissing noise, open a window and quickly leave the building, then turn off the main gas valve.
    - **Tsunami Risk:** If you live near the coast, be aware of tsunami warnings and move to higher ground immediately if advised.
    """)

with tab2:
    st.markdown("## 🛶 Floods")
    
    st.subheader("Hydrological Context")
    st.write("""
    Flooding represents an overflow of water onto normally dry land. It is driven by prolonged rainfall, rapid snowmelt, storm surges from the ocean, or the failure of water containment systems like dams or levees.
    - **Types of Floods:**
        - **River Floods:** Water levels rise over the top of river banks.
        - **Coastal Floods:** Caused by higher than average high tide and worsened by heavy rainfall and onshore winds.
        - **Flash Floods:** Rapid flooding of low-lying areas, typically caused by intense rainfall within a short window (under 6 hours).
    """)
    
    st.subheader("Operational Directives")
    st.markdown("""
    #### 1. Mitigation & Preparedness (Before)
    - **Assess Risk:** Know your area's flood risk and whether your property is in a flood plain.
    - **Elevate Utilities:** Raise your furnace, water heater, and electric panel if they are in areas of your home that may be flooded.
    - **Install Valves:** Install 'check valves' in sewer traps to prevent floodwater from backing up into the drains of your home.
    
    #### 2. Immediate Action (During)
    - **Turn Around, Don't Drown!** Do not walk, swim, or drive through floodwaters. 
        - Just **6 inches** of fast-moving water can knock over an adult.
        - Only **12 inches** of rushing water can carry away most cars, and **2 feet** can carry away SUVs and trucks.
    - **Evacuate the Zone:** Move to higher ground immediately. If told to evacuate, do so immediately.
    
    #### 3. Recovery Phase (After)
    - **Contamination Risk:** Floodwaters are often heavily contaminated with chemicals and raw sewage. Avoid contact and thoroughly wash any skin that touches the water.
    - **Electrical Safety:** Never touch electrical equipment if you are wet or standing in water.
    - **Mold Mitigation:** Dry out your home quickly. Anything that stays wet for 48 hours will likely grow mold and may need to be discarded.
    """)

with tab3:
    st.markdown("## 🧯 Fires")
    
    st.subheader("Combustion Context")
    st.write("""
    Fire is a chemical reaction—specifically, rapid oxidation—that produces heat and light. To exist, fire requires three elements, commonly known as the Fire Triangle:
    1. **Heat:** To raise the material to its ignition temperature.
    2. **Fuel:** The combustible material being burned.
    3. **Oxygen:** To sustain the combustion process.
    Removing any one of these three elements will extinguish a fire.
    """)
    
    st.subheader("Operational Directives")
    st.markdown("""
    #### 1. Mitigation & Preparedness (Before)
    - **Smoke Alarms:** Install alarms on every level of the home, inside bedrooms, and outside sleeping areas. Test them monthly.
    - **Defensible Space (Wildfires):** Clear dry brush, leaves, and pine needles within a 30-foot radius of your home to remove potential fuel.
    - **Escape Plans:** Create an escape plan with at least two established exits from every room in your house.
    
    #### 2. Immediate Action (During)
    - **Crawl Low:** Smoke is toxic and rises to the ceiling. Crawling keeps you in the safest, most breathable air.
    - **Checking Doors:** Use the back of your hand to feel a door or doorknob before opening it. If it is hot, the fire is on the other side—use an alternate exit.
    - **Stop, Drop, and Roll:** If your clothes ignite, instantly stop walking, drop to the ground, cover your face with your hands, and roll over continuously to smother the flames.
    
    #### 3. Recovery Phase (After)
    - **Wait for Clearance:** Do not re-enter the structure until the fire department officially declares it safe and structurally sound.
    - **Address Burns:** Cool severe burn areas with cool (not freezing) water, cover them loosely with a clean, dry cloth, and seek immediate medical attention.
    """)

with tab4:
    st.markdown("## 🌬️ Cyclones & Hurricanes")
    
    st.subheader("Meteorological Context")
    st.write("""
    A tropical cyclone is a rapidly rotating storm system characterized by a low-pressure center, a closed low-level atmospheric circulation, strong winds, and a spiral arrangement of thunderstorms that produce heavy rain.
    - **Terminology:** Called 'Hurricanes' in the North Atlantic, 'Typhoons' in the Northwest Pacific, and 'Cyclones' in the South Pacific/Indian Ocean.
    - **The Eye:** The system features a relatively calm, clear area at the exact center, called the eye. The eyewall surrounding it contains the most devastating winds.
    """)
    
    st.subheader("Operational Directives")
    st.markdown("""
    #### 1. Mitigation & Preparedness (Before)
    - **Storm Shutters:** Protect structural integrity by boarding up windows with permanent storm shutters or exterior grade plywood.
    - **Clean the Yard:** High winds can turn outdoor furniture, garbage cans, and toys into deadly flying projectiles. Bring them inside.
    - **Review Evacuation Routes:** Know the established local hurricane evacuation routes and have a destination planned.
    
    #### 2. Immediate Action (During)
    - **Take Refuge:** If not evacuated, stay indoors in a windowless interior room on the lowest non-flooding level (e.g., a closet or hallway).
    - **Beware the Eye:** If the storm suddenly becomes incredibly calm, you are likely in the eye. **Do not go outside.** The winds will violently return from the opposite direction momentarily.
    
    #### 3. Recovery Phase (After)
    - **Storm Surge:** Be aware that post-storm flooding is common. Storm surges (ocean water pushed ashore) cause the majority of hurricane-related fatalities.
    - **Downed Lines:** Treat all downed power lines in the area as live electric wires and maintain a massive distance.
    """)

with tab5:
    st.markdown("## 🏜️ Heatwaves")
    
    st.subheader("Meteorological Context")
    st.write("""
    A heatwave is a period of excessively hot weather, which may be accompanied by high humidity. They are typically created when high-pressure atmospheric systems slow down and compress the air, trapping warmer air closer to the ground and preventing cloud formation.
    - **Heat Index:** This measures what the temperature actually *feels* like to the human body when relative humidity is combined with the air temperature. High humidity prevents sweat from evaporating natively, causing the body to overheat faster.
    """)
    
    st.subheader("Operational Directives")
    st.markdown("""
    #### 1. Mitigation & Preparedness (Before)
    - **Cooling Infrastructure:** Ensure your air conditioning is functioning efficiently. Install window reflectors to project heat back outside.
    - **Identify Cooling Centers:** Know the locations of public libraries, malls, or dedicated municipal cooling shelters in case of power grid failure.
    
    #### 2. Immediate Action (During)
    - **Hydration is Key:** Drink plenty of water constantly, even if you do not feel thirsty. Avoid sugary, caffeinated, or alcoholic beverages as they accelerate dehydration.
    - **Rest & Reschedule:** Avoid strenuous outdoor physical activity, especially during the peak sun hours of 11:00 AM to 4:00 PM.
    - **Never Leave Dependents in Vehicles:** The internal temperature of a parked car can reach lethal levels in under 10 minutes, even with windows cracked.
    
    #### 3. Recognizing Heat Illness (After/During)
    - **Heat Exhaustion:** Symptoms include heavy sweating, weakness, cold/pale/clammy skin, and nausea. Move to a cooler area, sip water, and use cool compresses.
    - **Heat Stroke (Medical Emergency):** Symptoms include high body temperature (103°F+), hot/red/dry skin (no sweating), rapid pulse, and confusion or unconsciousness. Call 911 immediately and actively attempt to cool the person down with ice or water.
    """)
