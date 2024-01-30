# gp_clock.py
- This program shows a clock time display

# clock_function.py
- Its a function for gp_clock.py

# TPH.py
- This utilized `clock_function.py` to show clock and 
    - Temperature - Temperature in red
    - Pressure - Pressure in green
    - Humidity - Humidity in blue

# TPH.service
- Its a TPH service file for running this TPH.py python script at the startup.
- Link for this information - [link](https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/)
- Run following commands -
    ```bash
    sudo cp THP.service /etc/systemd/system/
    cd /etc/systemd/system
    chmod 644 TPH.service
    chmod +x TPH.service
    sudo systemctl daemon-reload
    sudo systemctl start TPH.service
    sudo systemctl enable TPH.service
    ```