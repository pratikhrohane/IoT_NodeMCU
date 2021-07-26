"""
ADC >>> Analog to Digital Convertor (SAR ADC in NodeMCU)
 <Successive-approximation-register>
Terms:
    Input Signal Frequency (Fin)
    Sampling rate of ADC
    Resolution of ADC (n - no. of bits)
    Nyquist Rate (2*Fin)
    Accuracy of ADC
    (minimum which cab be measured)
        Vref/(2^n - 1)

Example:
    Vref = 1V, Vin = 0.5V, Resolution is 10bits (Max value = 1023)
    Digital-Equivalent = (Vin/ Vref) * Full scale equivalent
                       = (0.5/1) * 1023
                       = 512
"""
import machine
import time


def main():
    adc_pin = machine.ADC(0)
    while True:
        print(adc_pin.read())
        time.sleep(1)


if __name__ == '__main__':
    main()
