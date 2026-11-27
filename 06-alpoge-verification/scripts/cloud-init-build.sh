#!/bin/bash
set -x
exec > /var/log/rh-setup.log 2>&1
shutdown -h +1440   # safety stop: the machine halts by itself after 24 h
apt-get update -y && apt-get install -y git curl build-essential zstd jq htop
useradd -m -s /bin/bash lean
cat > /home/lean/run.sh <<'EOS'
#!/bin/bash
set -x
cd ~
curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh -s -- -y --default-toolchain none
source ~/.elan/env
mkdir -p dl && cd dl
for i in $(seq -w 1 14); do curl -sL --retry 5 -o lean.tar.gz.part$i https://alpo.ge/lean.tar.gz.part$i; done
cat lean.tar.gz.part* > lean.tar.gz && sha256sum lean.tar.gz > ~/archive.sha256
cd ~ && tar xzf dl/lean.tar.gz && cd ~/lean
echo STAGE cache > ~/stage
lake exe cache get > ~/cache.log 2>&1
echo STAGE build > ~/stage
date > ~/build.start
/usr/bin/time -v lake build > ~/build.log 2>&1
echo $? > ~/build.exit
date > ~/build.end
cat > ~/lean/AxiomCheck.lean <<'EOL'
import Main
#check (riemannHypothesis : RiemannHypothesis)
#print axioms riemannHypothesis
#print axioms riemannZeta_eq_zero_re
#print axioms LFunction_ne_zero_of_half_lt_re
#print axioms LFunction_eq_zero_re
#print axioms LFunction_eq_zero_re_of_isPrimitive
EOL
lake env lean ~/lean/AxiomCheck.lean > ~/axioms.log 2>&1
echo STAGE done > ~/stage
EOS
chmod +x /home/lean/run.sh && chown -R lean:lean /home/lean
sudo -u lean -i bash -c 'nohup ~/run.sh > ~/run.log 2>&1 &'
