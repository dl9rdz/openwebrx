# Installation radiosonde decoder

## install Zilogs RS tool manually

- git clone https://github.com/rs1729/RS
- cd demod/mod
- make
- sudo cp *mod /usr/local/bin

(assuming that /usr/local/bin is on your default PATH)

Currently, RS41, DFM9, DFM17 (these three have been tested) and M10/M20 (untested) are supported.


# Installation of modified openwebrx+ with radiosonde support

## Based on pre-compiled OpenWebRX+ packages

- Start with a complete installation of OpenWebRX+ from https://luarvique.github.io/ppa/
- Obtain the modified version
  git clone https://github.com/dl9rdz/openwebrx

### Testing without installation

- Stop the standard openwebrx+
  sudo systemctl stop openwebrx
- cd openwebrx
- run "sudo -u openwebrx ./openwebrx.py"

### Installation and automated start of modified version
- In the "openwebrx" folder of the modified source run:
- sudo python3 ./setup.py install
- stop the service (sudo systemctl stop openwebrx)
- Modify /etc/systemd/system/multi-user.target.wants/openwebrx.service
  replace /usr/bin/openwebrx with the local version /usr/local/bin/openwebrx
