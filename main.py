from utils import check_float, round_to_1_sf
from BeltWindow import Ui_MainWindow as BeltScreen
from PySide6 import QtGui
from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
import math
import ctypes
from ctypes import wintypes
import sys

if getattr(sys, 'frozen', False):
    import pyi_splash


class BeltWindow(QMainWindow, BeltScreen):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(
            ".\\assets\\icons\\calculation.png"))
        self.setWindowTitle("Transmissions Calculator")

        # Input Fields validation
        self.inputValidator = QDoubleValidator(0.00, 9999999.99, 2)
        # Belt Inputs
        self.rev1Input.setValidator(self.inputValidator)
        self.rev2Input.setValidator(self.inputValidator)
        self.powerInput.setValidator(self.inputValidator)
        self.centerInput.setValidator(self.inputValidator)
        self.factorInput.setValidator(self.inputValidator)
        self.pitchInput.setValidator(self.inputValidator)
        self.beltLengthInput.setValidator(self.inputValidator)
        self.ratedPowerInput.setValidator(self.inputValidator)
        self.addPowerInput.setValidator(self.inputValidator)
        self.contactFactorInput.setValidator(self.inputValidator)
        self.powerFactorInput.setValidator(self.inputValidator)
        self.instAllowanceInput.setValidator(self.inputValidator)
        self.takeAllowanceInput.setValidator(self.inputValidator)
        self.smallPulleySelect.setChecked(True)
        # Chain Inputs
        self.chainPitchInput.setValidator(self.inputValidator)
        self.betweenWidthInput.setValidator(self.inputValidator)
        self.rollerDiameterInput.setValidator(self.inputValidator)
        self.plateDiameterInput.setValidator(self.inputValidator)
        self.innerWidthInput.setValidator(self.inputValidator)
        self.overallJointInput.setValidator(self.inputValidator)
        self.pinDiameterInput.setValidator(self.inputValidator)
        self.tranversePitchInput.setValidator(self.inputValidator)
        self.massInput.setValidator(self.inputValidator)
        self.breakingLoadInput.setValidator(self.inputValidator)
        self.transmissionRatioInput.setValidator(self.inputValidator)
        self.chainRatedPowerInput.setValidator(self.inputValidator)
        self.serviceFactorInput.setValidator(self.inputValidator)
        self.teethInput.setValidator(self.inputValidator)
        self.centerDistanceInput.setValidator(self.inputValidator)
        self.initialSagInput.setValidator(self.inputValidator)
        self.chainRev1Input.setValidator(self.inputValidator)
        self.constantInput.setValidator(self.inputValidator)
        self.loadFactorInput.setValidator(self.inputValidator)
        self.bearingAreaInput.setValidator(self.inputValidator)
        self.smallSprocketSelect.setChecked(True)

        # Buttons
        # Belt drive
        self.calculateButton.clicked.connect(self.calculations)
        self.nextButton.clicked.connect(self.next_tab)
        self.clearInputButton.clicked.connect(self.clear_input)
        self.clearResultButton.clicked.connect(self.clear_results)
        self.clearAllButton.clicked.connect(self.clear_all)
        # Chain drive
        self.chainCalculateButton.clicked.connect(self.chain_calculations)
        self.prevButton.clicked.connect(self.prev_tab)
        self.chainClearInputsBtn.clicked.connect(self.chain_clear_input)
        self.chainClearResultsBtn.clicked.connect(self.chain_clear_results)
        self.chainClearAll.clicked.connect(self.chain_clear_all)

        # Tab Widgets
        # self.transmissions.currentChanged.connect(self.tabChanged)

    def next_tab(self):
        self.transmissions.setCurrentIndex(1)

    def prev_tab(self):
        self.transmissions.setCurrentIndex(0)

    def tabChanged(self, index):
        if index == 0:
            self.transmissions.setFixedHeight(991)
            self.centralwidget.setFixedHeight(1011)
            self.setFixedHeight(1065)
        elif index == 1:
            self.transmissions.setFixedHeight(1141)
            self.centralwidget.setFixedHeight(1163)
            self.setFixedHeight(1212)

    def clear_input(self):
        self.rev1Input.setText("")
        self.rev2Input.setText("")
        self.powerInput.setText("")
        self.centerInput.setText("")
        self.factorInput.setText("")
        self.pitchInput.setText("")
        self.beltLengthInput.setText("")
        self.ratedPowerInput.setText("")
        self.addPowerInput.setText("")
        self.contactFactorInput.setText("")
        self.powerFactorInput.setText("")
        self.instAllowanceInput.setText("")
        self.takeAllowanceInput.setText("")

    def clear_results(self):
        self.resultText.setText("")
        self.speedRatioOutput.setText("")
        self.designPowerOutput.setText("")
        self.pulleyDiameterOutput.setText("")
        self.beltLengthOutput.setText("")
        self.exactCenterOutput.setText("")
        self.powerRatingOutput.setText("")
        self.beltNumberOutput.setText("")
        self.beltSpeedOutput.setText("")
        self.effectiveTensionOutput.setText("")
        self.torqueOutput.setText("")
        self.tightOutput.setText("")
        self.slackOutput.setText("")
        self.tensionRatioOutput.setText("")
        self.staticTensionOutput.setText("")
        self.shaftLoadOutput.setText("")
        self.contactAngleOutput.setText("")
        self.wrapAngleOutput.setText("")
        self.wrapAngleOutput_2.setText("")

    def clear_all(self):
        self.clear_input()
        self.clear_results()

    def chain_clear_input(self):
        self.chainPitchInput.setText("")
        self.betweenWidthInput.setText("")
        self.rollerDiameterInput.setText("")
        self.plateDiameterInput.setText("")
        self.innerWidthInput.setText("")
        self.overallJointInput.setText("")
        self.pinDiameterInput.setText("")
        self.tranversePitchInput.setText("")
        self.massInput.setText("")
        self.breakingLoadInput.setText("")
        self.transmissionRatioInput.setText("")
        self.chainRatedPowerInput.setText("")
        self.serviceFactorInput.setText("")
        self.teethInput.setText("")
        self.centerDistanceInput.setText("")
        self.initialSagInput.setText("")
        self.chainRev1Input.setText("")
        self.constantInput.setText("")
        self.loadFactorInput.setText("")
        self.bearingAreaInput.setText("")

    def chain_clear_results(self):
        self.chainResults.setText("")

    def chain_clear_all(self):
        self.chain_clear_input()
        self.chain_clear_results()

    def calculations(self):
        try:
            # Inputs
            rev1 = self.rev1Input.text()
            rev2 = self.rev2Input.text()
            power = self.powerInput.text()
            centre = self.centerInput.text()
            factor = self.factorInput.text()
            pitch = self.pitchInput.text()
            big_pulley = self.bigPulleySelect.isChecked()
            crossBelt = self.crossBelt.isChecked()
            beltLength = self.beltLengthInput.text()
            ratedPower = self.ratedPowerInput.text()
            addPower = self.addPowerInput.text()
            contactFactor = self.contactFactorInput.text()
            powerFactor = self.powerFactorInput.text()
            installAllowance = self.instAllowanceInput.text()
            takeAllowance = self.takeAllowanceInput.text()
            beltWeight = self.beltWeightInput.text()

            # Check
            if (not check_float(rev1) or not check_float(rev2)
                or not check_float(power) or not check_float(centre)
                    or not check_float(factor) or not check_float(pitch)
                    or not check_float(beltLength) or not check_float(ratedPower)
                    or not check_float(addPower) or not check_float(contactFactor)
                    or not check_float(powerFactor) or not check_float(beltWeight)
                    or not check_float(installAllowance) or not check_float(takeAllowance)):
                QMessageBox.critical(
                    self, "Error with input fields", "<p style='font-weight:semibold;font-size:16px;'>All fields are required.<p><p>Also, confirm that they are numbers!</p>")
                return

            # Calculations
            speed_ratio = round(float(rev1)/float(rev2), 2)
            design_power = round(float(power)*float(factor), 2)
            pitch_diameter = round((float(pitch)*float(rev2))/float(rev1),
                                   2) if big_pulley else round((float(rev1)*float(pitch))/float(rev2), 2)
            A = round((float(beltLength)/4) -
                      (0.3925*(float(pitch)+pitch_diameter)), 2)
            B = round(((float(pitch)-pitch_diameter)**2)/8,
                      2) if big_pulley else round(((pitch_diameter-float(pitch))**2)/8, 2)
            exact_center = round(A + math.sqrt((A**2)-B))
            power_rating = round(float(ratedPower)+float(addPower), 2)
            belt_number = round(
                (design_power/(power_rating*float(contactFactor)*float(powerFactor))))
            belt_speed = round(((math.pi*pitch_diameter*float(rev1))/(60*1000)),
                               1) if big_pulley else round(((math.pi*float(pitch)*float(rev1))/(60*1000)), 1)
            static_tension = round(((0.9*((500 * (((2.5-float(contactFactor))*design_power)/(
                float(contactFactor)*belt_number*belt_speed)))+(float(beltWeight)*(belt_speed**2))))), 2)
            if crossBelt:
                belt_length = round((2*float(exact_center))+((math.pi/2)*(pitch_diameter+float(pitch)))+(
                    (float(pitch)+pitch_diameter)**2/(4*float(exact_center))), 2)
                belt_string = f"""
                    <p class='eq-c'>Belt Length (<var>L</var>) = 2<var>C</var> + <span class='fraction'><span class='fup'><var>π</var></span><span class='bar'>/</span><span class='fdn'>2</span></span>(<var>D<sub>2</sub></var> + <var>D<sub>1</sub></var>) + <span class='fraction'><span class='fup'>(<var>D<sub>1</sub></var> + <var>D<sub>2</sub></var>)<sup>2</sup></span><span class='bar'>/</span><span class='fdn'>4<var>C</var></span></span></p>
                    <p class='eq-c'>Belt Length (<var>L<sub>P</sub></var>) = 2({exact_center}) + <span class='fraction'><span class='fup'><var>π</var></span><span class='bar'>/</span><span class='fdn'>2</span></span>({pitch} + {pitch_diameter}) + <span class='fraction'><span class='fup'>({pitch} + {pitch_diameter})<sup>2</sup></span><span class='bar'>/</span><span class='fdn'>4({exact_center})</span></span></p>
                """

                wrap_angle = round(
                    180 + (2 * (math.degrees(math.asin((float(pitch)+pitch_diameter)/(2*exact_center))))))
                angle_string = f"""
                    <p class='eq-c'>Angle of wrap of larger pulley (<var>a<sub>1</sub></var>) = Angle of wrap of smaller pulley (<var>a<sub>2</sub></var>) = 180 + 2<var>sin⁡<sup>-1</sup></var>(<span class='fraction'><span class='fup'><var>D</var> + <var>d</var></span><span class='bar'>/</span><span class='fdn'>2C</span></span>)</p>
                    <p class='eq-c'>Angle of wrap of larger pulley (<var>a<sub>1</sub></var>) = Angle of wrap of smaller pulley (<var>a<sub>2</sub></var>) = 180 + 2<var>sin⁡<sup>-1</sup></var>(<span class='fraction'><span class='fup'>{pitch} + {pitch_diameter}</span><span class='bar'>/</span><span class='fdn'>2({exact_center})</span></span>)</p>
                    <p>Angle of wrap of larger pulley (<var>a<sub>1</sub></var>) = Angle of wrap of smaller pulley (<var>a<sub>2</sub></var>) = {wrap_angle}<sup>°</sup></p>
                """

                contact_angle = round(
                    math.degrees(math.asin((float(pitch)+pitch_diameter)/exact_center)))
                contact_string = f"""
                <p class='eq-c'>Belt contact angle (<var>sin⁡<sup>-1</sup>β</var>) = <span class='fraction'><span class='fup'><var>D</var> + <var>d</var></span><span class='bar'>/</span><span class='fdn'><var>C</var></span></span></p>
                <p class='eq-c'>Belt contact angle (<var>sin⁡<sup>-1</sup>β</var>) = <span class='fraction'><span class='fup'>{pitch} + {pitch_diameter}</span><span class='bar'>/</span><span class='fdn'>{exact_center}</span></span></p>
                <p>Belt contact angle (<var>β</var>) = {contact_angle}°</p>
                """

            else:
                belt_length = round((2*float(centre))+((math.pi/2)*(pitch_diameter+float(pitch)))+((float(pitch)-pitch_diameter)**2/(4*float(centre))),
                                    2) if big_pulley else round((2*float(centre))+((math.pi/2)*(pitch_diameter+float(pitch)))+((pitch_diameter-float(pitch))**2/(4*float(centre))), 2)
                belt_string = f"""
                    <p class='eq-c'>Belt Length (<var>L<sub>P</sub></var>) = 2<var>C</var> + <span class='fraction'><span class='fup'><var>π</var></span><span class='bar'>/</span><span class='fdn'>2</span></span>(<var>D</var> + <var>d</var>) + <span class='fraction'><span class='fup'>(<var>D</var> - <var>d</var>)<sup>2</sup></span><span class='bar'>/</span><span class='fdn'>4<var>C</var></span></span></p>
                    <p class='eq-c'>Belt Length (<var>L<sub>P</sub></var>) = {f"2({centre}) + <span class='fraction'><span class='fup'><var>π</var></span><span class='bar'>/</span><span class='fdn'>2</span></span>({pitch} + {pitch_diameter}) + <span class='fraction'><span class='fup'>({pitch} - {pitch_diameter})<sup>2</sup></span><span class='bar'>/</span><span class='fdn'>4({centre})</span></span>" if big_pulley else f"2({centre}) + <span class='fraction'><span class='fup'><var>π</var></span><span class='bar'>/</span><span class='fdn'>2</span></span>({pitch_diameter} + {pitch}) + <span class='fraction'><span class='fup'>({pitch_diameter} - {pitch})<sup>2</sup></span><span class='bar'>/</span><span class='fdn'>4({centre})</span></span>"}</p>
                """

                wrap_angle1 = round(180-(2 * (math.degrees(math.asin((float(pitch)-pitch_diameter)/(2*exact_center))))
                                         ) if big_pulley else 180-(2 * (math.degrees(math.asin((pitch_diameter-float(pitch))/(2*exact_center))))))
                wrap_angle2 = round(180+(2 * (math.degrees(math.asin((float(pitch)-pitch_diameter)/(2*exact_center))))
                                         ) if big_pulley else 180+(2 * (math.degrees(math.asin((pitch_diameter-float(pitch))/(2*exact_center))))))
                angle_string = f"""
                    <p class='eq-c'>Angle of wrap of larger pulley (<var>a<sub>1</sub></var>) = 180 - 2<var>sin⁡<sup>-1</sup></var>(<span class='fraction'><span class='fup'><var>D</var> - <var>d</var></span><span class='bar'>/</span><span class='fdn'>2C</span></span>)</p>
                    <p class='eq-c'>Angle of wrap of larger pulley (<var>a<sub>1</sub></var>) = {f"180 - 2<var>sin⁡<sup>-1</sup></var>(<span class='fraction'><span class='fup'>{pitch} - {pitch_diameter}</span><span class='bar'>/</span><span class='fdn'>2({exact_center})</span></span>)" if big_pulley else f"180 - 2<var>sin⁡<sup>-1</sup></var>(<span class='fraction'><span class='fup'>{pitch_diameter} - {pitch}</span><span class='bar'>/</span><span class='fdn'>2({exact_center})</span></span>)"}</p>
                    <p>Angle of wrap of larger pulley (<var>a<sub>1</sub></var>) = {wrap_angle1}<sup>°</sup></p>
                    <p class='eq-c'>Angle of wrap of smaller pulley (<var>a<sub>2</sub></var>) = 180 + 2<var>sin⁡<sup>-1</sup></var>(<span class='fraction'><span class='fup'><var>D</var> - <var>d</var></span><span class='bar'>/</span><span class='fdn'>2C</span></span>)</p>
                    <p class='eq-c'>Angle of wrap of smaller pulley (<var>a<sub>2</sub></var>) = {f"180 + 2<var>sin⁡<sup>-1</sup></var>(<span class='fraction'><span class='fup'>{pitch} - {pitch_diameter}</span><span class='bar'>/</span><span class='fdn'>2({exact_center})</span></span>)" if big_pulley else f"180 + 2<var>sin⁡<sup>-1</sup></var>(<span class='fraction'><span class='fup'>{pitch_diameter} - {pitch}</span><span class='bar'>/</span><span class='fdn'>2({exact_center})</span></span>)"}</p>
                    <p>Angle of wrap of smaller pulley (<var>a<sub>2</sub></var>) = {wrap_angle2}<sup>°</sup></p>
                """
                contact_angle = round(math.degrees(math.asin((float(pitch)-pitch_diameter)/exact_center)
                                                   )) if big_pulley else round(math.degrees(math.asin((pitch_diameter-float(pitch))/exact_center)))
                contact_string = f"""
                <p class='eq-c'>Belt contact angle (<var>sin⁡<sup>-1</sup>β</var>) = <span class='fraction'><span class='fup'><var>D</var> - <var>d</var></span><span class='bar'>/</span><span class='fdn'><var>C</var></span></span></p>
                <p class='eq-c'>Belt contact angle (<var>sin⁡<sup>-1</sup>β</var>) = {f"<span class='fraction'><span class='fup'>{pitch} - {pitch_diameter}</span><span class='bar'>/</span><span class='fdn'>{exact_center}</span></span>" if big_pulley else f"<span class='fraction'><span class='fup'>{pitch_diameter} - {pitch}</span><span class='bar'>/</span><span class='fdn'>{exact_center}</span></span>"}</p>
                <p>Belt contact angle (<var>β</var>) = {contact_angle}°</p>
                """

            effective_tension = round((1000*float(power))/belt_speed)
            torque = round((effective_tension * pitch_diameter)/2000,
                           2) if big_pulley else round((effective_tension * float(pitch))/2000, 1)
            tight_tension = round((((1000*design_power)/(belt_number*belt_speed)) *
                                   (2.5/(2*float(contactFactor))))+(float(beltWeight)*(belt_speed**2)), 2)
            slack_tension = round((((1000*design_power)/(belt_number*belt_speed)) *
                                   ((2.5-(2*float(contactFactor)))/(2*float(contactFactor))))+(float(beltWeight)*(belt_speed**2)), 2)
            tension_ratio = round(tight_tension/slack_tension)

            static_load = round(
                (1.5 * (2*belt_number*static_tension*(math.sin(math.radians(contact_angle/2))))), 2)
            static_string = f"""
                <p class='eq-c'>Static shaft load (<var>L<sub>s</sub></var>) = 1.5(2<var>N</var> * <var>T<sub>m</sub></var> * sin(<span class='fraction'><span class='fup'>β</span><span class='bar'>/</span><span class='fdn'>2</span>)</span>)</p>
                <p class='eq-c'>Static shaft load (<var>L<sub>s</sub></var>) = 1.5(2({belt_number}) * {static_tension} * sin(<span class='fraction'><span class='fup'>{contact_angle}</span><span class='bar'>/</span><span class='fdn'>2</span>)</span>)</p>
                <p>Static shaft load (<var>L<sub>s</sub></var>) = {static_load}N</p>
                """

            # results
            result = self.resultText

            result.setText(f"""
                            <p style='font-weight:bold;font-size:16px'>1. Determination of Speed Ratio (<var>S<sub>r</sub></var>)</p>
                            <p class='eq-c'>Speed Ratio (<var>S<sub>r</sub></var>) = <span class='fraction'><span class='fup'><var>N<sub>1</sub></var></span><span class='bar'>/</span><span class='fdn'><var>N<sub>2</sub></var></span></span></p>
                            <p class='eq-c'>Speed Ratio (<var>S<sub>r</sub></var>) = <span class='fraction'><span class='fup'>{rev1}</span><span class='bar'>/</span><span class='fdn'>{rev2}</span></span></p>
                            <p>Speed Ratio (<var>S<sub>r</sub></var>) = {speed_ratio}</p><br/>
                            
                            <p style='font-weight:bold;font-size:16px'>2. Determination of Design Power (<var>P<sub>D</sub></var>)</p>
                            <p class='eq-c'>Design Power (<var>P<sub>D</sub></var>) = <var>P</var> * <var>K</var></p>
                            <p class='eq-c'>Design Power (<var>P<sub>D</sub></var>) = {power} * {factor}</p>
                            <p>Design Power (<var>P<sub>D</sub></var>) = {design_power} kw</p><br/>
                            
                            <p style='font-weight:bold;font-size:16px'>3. Determination of {"Smaller pulley pitch Diameter (d)" if big_pulley else "Bigger puller Pitch Diameter (D)"}</p>
                            <p class='eq-c'>Speed Ratio <span class='fraction'><span class='fup'><var>N<sub>1</sub></var></span><span class='bar'>/</span><span class='fdn'><var>N<sub>2</sub></var></span></span> = <span class='fraction'><span class='fup'><var>D</var></span><span class='bar'>/</span><span class='fdn'><var>d</var></span></span></p>
                            <p class='eq-c'>{"Smaller pulley pitch Diameter (d)" if big_pulley else "Bigger puller Pitch Diameter (D)"} = {f"<span class='fraction'><span class='fup'>{rev2} * {pitch}</span><span class='bar'>/</span><span class='fdn'>{rev1}</span></span>" if big_pulley else f"<span class='fraction'><span class='fup'>{rev1} * {pitch}</span><span class='bar'>/</span><span class='fdn'>{rev2}</span></span>"} </p>
                            <p class='eq-c'>{"Smaller pulley pitch Diameter (d)" if big_pulley else "Bigger puller Pitch Diameter (D)"} = {pitch_diameter}mm</p><br/>
                            
                            <p style='font-weight:bold;font-size:16px'>4. Determination of Belt Length (<var>L<sub>P</sub></var>)</p>
                            {belt_string}
                            <p>Belt Length (<var>L<sub>P</sub></var>) = {belt_length}mm</p><br/>
                            
                            <p style='font-weight:bold;font-size:16px'>5. Determination of exact Centre Distance (<var>C</var>)</p>                           
                            <p class='eq-c'>Centre Distance (<var>C</var>) = <var>A</var> + <span class="radical">√</span><span class="radicand"><var>A</var><sup>2</sup> - <var>B</var></span></p>
                            <p class='eq-c' style='margin-left:5px'>Where: <var>A</var> = <span class='fraction'><span class='fup'><var>L</var></span><span class='bar'>/</span><span class='fdn'>4</span></span> - 0.3925(<var>D</var> + <var>d</var>) </p>
                            <p class='eq-c' style='margin-left:5px'>Where: <var>A</var> = {A} </p>
                            <p class='eq-c' style='margin-left:5px'>Where: <var>B</var> = <span class='fraction'><span class='fup'>(<var>D</var> - <var>d</var>)<sup>2</sup></span><span class='bar'>/</span><span class='fdn'>8</span></span></p>
                            <p style='margin-left:5px'>Where: <var>B</var> = {B} </p>
                            <p class='eq-c'>centre Distance (<var>C</var>) = {A} + <span class="radical">√</span><span class="radicand">{A}<sup>2</sup> - {B}</span></p>
                            <p class='eq-c'>Centre Distance (<var>C</var>) = {exact_center}mm</p>
                            <p style='font-weight:medium'>Installation and Take-up allowance for centre distance:</p>
                            <p>Minimum centre distance = <var>C</var> - <var>installation allowance</var></p>
                            <p>Minimum centre distance = {exact_center} - {installAllowance} = {float(exact_center) - float(installAllowance)}mm </p>
                            <p>Maximum Centre distance = <var>C</var> + <var>Take-up allowance</var></p>
                            <p>Maximum Centre distance = {exact_center} + {takeAllowance} = {float(exact_center) + float(takeAllowance)}mm </p>
                            <br/>
                            
                            <p style='font-weight:bold;font-size:16px'>6. Determination of Power Rating</p>
                            <p>Power Rating (<var>p</var>) = <var>Rated power</var> + <var>Additional Power for speed ratio</var></p>
                            <p>Power Rating (<var>p</var>) = {ratedPower} + {addPower} = {power_rating}kw </p>
                            <br/>
                            
                            <p style='font-weight:bold;font-size:16px'>7. Determination of Number of Belts</p>
                            <p class='eq-c'>Number of Belts (<var>N</var>) = <span class='fraction'><span class='fup'><var>P<sub>D</sub></var></span><span class='bar'>/</span><span class='fdn'><var>p</var> * <var>F<sub>A</sub></var> * <var>F<sub>L</sub></var></span></span></p>
                            <p class='eq-c'>Number of Belts (<var>N</var>) = <span class='fraction'><span class='fup'>{design_power}</span><span class='bar'>/</span><span class='fdn'>{power_rating} * {contactFactor} * {powerFactor}</span></span></p>
                            <p>Number of Belts (<var>N</var>) = {belt_number}</p>
                            <br/>
                            
                            <p style='font-weight:bold;font-size:16px'>8. Determination of Belt Speed</p>
                            <p class='eq-c'>Belt Speed (<var>V</var>) = <span class='fraction'><span class='fup'><var>π</var> * <var>d</var> * <var>N<sub>1</sub></var></span><span class='bar'>/</span><span class='fdn'>60 * 1000</span></p>
                            <p class='eq-c'>Belt Speed (<var>V</var>) = <span class='fraction'><span class='fup'><var>π</var> * <var>{pitch_diameter if big_pulley else pitch}</var> * <var>{rev1}</span><span class='bar'>/</span><span class='fdn'>60 * 1000</span></p>
                            <p>Belt Speed (<var>V</var>) = {belt_speed}m/s</p>
                            <br/>
                            
                            <p style='font-weight:bold;font-size:16px'>9. Determination of Effective Tension</p>
                            <p class='eq-c'>Effective Tension (<var>T<sub>e</sub></var>) = <span class='fraction'><span class='fup'>1000 * <var>P</var></span><span class='bar'>/</span><span class='fdn'><var>V</var></span></span></p>
                            <p class='eq-c'>Effective Tension (<var>T<sub>e</sub></var>) = <span class='fraction'><span class='fup'>1000 * {power}</span><span class='bar'>/</span><span class='fdn'>{belt_speed}</span></span></p>
                            <p>Effective Tension (<var>T<sub>e</sub></var>) = {effective_tension}N</p>
                            <br/>
                            
                            <p style='font-weight:bold;font-size:16px'>10. Determination of Torque</p>
                            <p class='eq-c'>Torque (<var>T<sub>q</sub></var>) = <span class='fraction'><span class='fup'><var>T<sub>e</sub></var> * <var>d</var></span><span class='bar'>/</span><span class='fdn'>2000</span></p>
                            <p class='eq-c'>Torque (<var>T<sub>q</sub></var>) = {f"<span class='fraction'><span class='fup'>{effective_tension} * {pitch_diameter}</span><span class='bar'>/</span><span class='fdn'>2000</span>" if big_pulley else f"<span class='fraction'><span class='fup'>{effective_tension} * {pitch}</span><span class='bar'>/</span><span class='fdn'>2000</span>"}</p>
                            <p>Torque (<var>T<sub>q</sub></var>) = {torque}N.m</p>
                            <br/>
                            
                            <p style='font-weight:bold;font-size:16px'>10. Determination of Tight Side Tension</p>
                            <p class='eq-c'>Tight Side Tension (<var>T<sub>t</sub></var>) = <span class='fraction'><span class='fup'>1000*<var>P<sub>D</sub></var></span><span class='bar'>/</span><span class='fdn'><var>N</var> * <var>V</var></span> * <span class='fraction'><span class='fup'>2.5</span><span class='bar'>/</span><span class='fdn'>2 * <var>F<sub>A</sub></var></span> + (<var>W</var> * <var>V<sup>2</sup></var>)</p>
                            <p class='eq-c'>Tight Side Tension (<var>T<sub>t</sub></var>) = {f"<span class='fraction'><span class='fup'>1000*{design_power}</span><span class='bar'>/</span><span class='fdn'>{belt_number} * {belt_speed}</span> * <span class='fraction'><span class='fup'>2.5</span><span class='bar'>/</span><span class='fdn'>2 * {contactFactor}</span> + ({beltWeight} * {belt_speed}<sup>2</sup>)"}</p>
                            <p>Tight Side Tension (<var>T<sub>t</sub></var>) = {tight_tension}N</p>
                            <br/>
                            
                            <p style='font-weight:bold;font-size:16px'>11. Determination of Slack Side Tension</p>
                            <p class='eq-c'>Slack Side Tension (<var>T<sub>s</sub></var>) = <span class='fraction'><span class='fup'>1000*<var>P<sub>D</sub></var></span><span class='bar'>/</span><span class='fdn'><var>N</var> * <var>V</var></span> * <span class='fraction'><span class='fup'>2.5 - (2<var>F<sub>A</sub></var>)</span><span class='bar'>/</span><span class='fdn'>2 * <var>F<sub>A</sub></var></span> + (<var>W</var> * <var>V<sup>2</sup></var>)</p>
                            <p class='eq-c'>Slack Side Tension (<var>T<sub>s</sub></var>) = {f"<span class='fraction'><span class='fup'>1000*{design_power}</span><span class='bar'>/</span><span class='fdn'>{belt_number} * {belt_speed}</span> * <span class='fraction'><span class='fup'>2.5 - 2({contactFactor})</span><span class='bar'>/</span><span class='fdn'>2 * {contactFactor}</span> + ({beltWeight} * {belt_speed}<sup>2</sup>)"}</p>
                            <p>Slack Side Tension (<var>T<sub>s</sub></var>) = {slack_tension}N</p>
                            <br/>
                            
                            <p style='font-weight:bold;font-size:16px'>12. Determination of Tension Ratio</p>
                            <p class='eq-c'>Tension Ratio (<var>T<sub>r</sub></var>) = <span class='fraction'><span class='fup'><var>T<sub>t</sub></var></span><span class='bar'>/</span><span class='fdn'><var>T<sub>s</sub></var></span></span></p>
                            <p class='eq-c'>Tension Ratio (<var>T<sub>r</sub></var>) = <span class='fraction'><span class='fup'>{tight_tension}</span><span class='bar'>/</span><span class='fdn'>{slack_tension}</span></span></p>
                            <p>Tension Ratio (<var>T<sub>r</sub></var>) = {tension_ratio}</p>
                            <br/>                           
                            
                            <p style='font-weight:bold;font-size:16px'>13. Determination of Minimum Static Tension</p>
                            <p class='eq-c'>Minimum static tension (<var>T<sub>m</sub></var>) = 0.9{{ 500 * <span class='fraction'><span class='fup'>(2.5 - <var>F<sub>A</sub></var>)<var>P<sub>D</sub></var></span><span class='bar'>/</span><span class='fdn'><var>F<sub>A</sub></var> * <var>N</var> * <var>V</var></span></span> + <var>W</var> * <var>V<sup>2</sup></var>}}</p>
                            <p class='eq-c'>Minimum static tension (<var>T<sub>m</sub></var>) = 0.9{{ 500 * <span class='fraction'><span class='fup'>(2.5 - {contactFactor}){design_power}</span><span class='bar'>/</span><span class='fdn'>{contactFactor} * {belt_number} * {belt_speed}</span></span> + {beltWeight} * {belt_speed}<sup>2</sup>}}</p>
                            <p>Minimum static tension (<var>T<sub>m</sub></var>) = {static_tension}N</p>
                            <br/>   
                            
                            <p style='font-weight:bold;font-size:16px'>14. Determination of Belt Contact Angle</p>
                            {contact_string}
                            <br/>                        
                            
                            <p style='font-weight:bold;font-size:16px'>15. Determination of Static Shaft Load</p>
                            {static_string}
                            <br/>
                            
                            <p style='font-weight:bold;font-size:16px'>16. Determination of Angle of Wrap</p>
                            {angle_string}
                            <br/>
                            
                            
                            """)
            self.speedRatioOutput.setText(f"{speed_ratio}")
            self.designPowerOutput.setText(f"{design_power} kw")
            self.pulleyDiameterOutput.setText(f"{pitch_diameter} mm")
            self.beltLengthOutput.setText(f"{belt_length} mm")
            self.exactCenterOutput.setText(f"{exact_center} mm")
            self.powerRatingOutput.setText(f"{power_rating} kw")
            self.beltNumberOutput.setText(f"{belt_number}")
            self.beltSpeedOutput.setText(f"{belt_speed} m/s")
            self.effectiveTensionOutput.setText(f"{effective_tension} N")
            self.torqueOutput.setText(f"{torque} N.m")
            self.tightOutput.setText(f"{tight_tension} N")
            self.slackOutput.setText(f"{slack_tension} N")
            self.tensionRatioOutput.setText(f"{tension_ratio}")
            self.staticTensionOutput.setText(f"{static_tension} N")
            self.shaftLoadOutput.setText(f"{static_load} N")
            self.contactAngleOutput.setText(f"{contact_angle}°")
            self.wrapAngleOutput.setText(f"{wrap_angle1}°")
            self.wrapAngleOutput_2.setText(f"{wrap_angle2}°")

        except Exception as e:
            QMessageBox.critical(
                self, "App Error", str(e) if not hasattr(e, 'message') else str(e.message))
            return

    def chain_calculations(self):
        try:
            # Inputs
            pitch = self.chainPitchInput.text()
            betweenWidth = self.betweenWidthInput.text()
            rollerDiameter = self.rollerDiameterInput.text()
            plateDiameter = self.plateDiameterInput.text()
            innerWidth = self.innerWidthInput.text()
            overallJoint = self.overallJointInput.text()
            bodyDiameter = self.pinDiameterInput.text()
            transversePitch = self.tranversePitchInput.text()
            mass = self.massInput.text()
            bearingArea = self.bearingAreaInput.text()
            breakingLoad = self.breakingLoadInput.text()
            transmissionRatio = self.transmissionRatioInput.text()
            ratedPower = self.chainRatedPowerInput.text()
            serviceFactor = self.serviceFactorInput.text()
            teethNumber = self.teethInput.text()
            smallSprocket = self.smallSprocketSelect.isChecked()
            centerDistance = self.centerDistanceInput.text()
            initialSag = self.initialSagInput.text()
            rev1 = self.chainRev1Input.text()
            constant = self.constantInput.text()
            loadFactor = self.loadFactorInput.text()

            # Check
            if (not check_float(rev1) or not check_float(pitch)
                or not check_float(betweenWidth) or not check_float(rollerDiameter)
                    or not check_float(plateDiameter) or not check_float(innerWidth)
                    or not check_float(overallJoint) or not check_float(ratedPower)
                    or not check_float(bodyDiameter) or not check_float(transversePitch)
                    or not check_float(mass) or not check_float(bearingArea)
                    or not check_float(breakingLoad) or not check_float(transmissionRatio)
                    or not check_float(serviceFactor) or not check_float(teethNumber)
                    or not check_float(centerDistance) or not check_float(initialSag)
                    or not check_float(constant) or not check_float(loadFactor)):
                QMessageBox.critical(
                    self, "Error with input fields", "<p style='font-weight:semibold;font-size:16px;'>All fields are required.<p><p>Also, confirm that they are numbers!</p>")
                return

            # Calculations
            teethNumber2 = round(float(transmissionRatio)*int(teethNumber)
                                 ) if smallSprocket else round(float(teethNumber)/float(transmissionRatio))
            sprocket_diameter1 = round((float(pitch)/math.sin(math.radians(180/int(teethNumber))))
                                       ) if smallSprocket else round((float(pitch)/math.sin(math.radians(180/int(teethNumber2)))))
            sprocket_diameter2 = round((float(pitch)/math.sin(math.radians(180/teethNumber2)))
                                       ) if smallSprocket else round((float(pitch)/math.sin(math.radians(180/int(teethNumber)))))
            design_power = round((float(serviceFactor)*float(ratedPower)), 2)
            number_links = round(((2*(float(centerDistance)/float(pitch)))+((int(teethNumber)+teethNumber2)/2)+(
                (((teethNumber2-int(teethNumber))/(2*math.pi))**2)*(float(pitch)/float(centerDistance))))) if smallSprocket else round(((2*(float(centerDistance)/float(pitch)))+((teethNumber2+int(teethNumber))/2)+(
                    (((int(teethNumber)-teethNumber2)/(2*math.pi))**2)*(float(pitch)/float(centerDistance)))))
            final_center = round((float(pitch)/4)*((number_links-((int(teethNumber)+teethNumber2)/2))+math.sqrt((number_links-((int(teethNumber)+teethNumber2)/2))**2-(8*(((teethNumber2-int(teethNumber))/(2*math.pi))**2)))), 2) if smallSprocket else round(
                (float(pitch)/4)*((number_links-((int(teethNumber2)+int(teethNumber))/2))+math.sqrt((number_links-((int(teethNumber2)+int(teethNumber))/2))**2-(8*(((int(teethNumber)-int(teethNumber2))/(2*math.pi))**2)))), 2)
            chain_length = round((number_links * float(pitch)), 1)
            chain_velocity = round(((math.pi*sprocket_diameter1*float(rev1))/(60*1000)),
                                   1) if smallSprocket else round(((math.pi*sprocket_diameter2*float(rev1))/(60*1000)), 1)
            chain_load = round((float(ratedPower)/(chain_velocity)), 3)
            factor_of_safety = round(float(breakingLoad)/(chain_load*1000))
            breaking_power = round(
                (float(breakingLoad)*chain_velocity)/(102*factor_of_safety*float(serviceFactor)), 2)
            bearing_load = round((chain_load*1000)/float(bearingArea), 2)
            bearing_power = round(
                (bearing_load * float(bearingArea) * chain_velocity)/(102*float(serviceFactor)), 2)
            tangential_force = round((102*design_power)/chain_velocity, 2)
            centrifugal_tension = round(float(mass)*(chain_velocity**2), 2)
            sagging_tension = round(
                float(constant) * float(mass) * 9.8 * (final_center/1000), 2)
            total_tension = round(
                (tangential_force + centrifugal_tension + sagging_tension))
            shaft_load = round(tangential_force * float(loadFactor))

            # Results
            result = self.chainResults

            result.setText(f"""                        
                           <p style='font-weight:bold;font-size:16px'>1. Determination of Number of teeth</p>
                           <span class='eq-c'>Number of teeth (<var>Z<sub>{'2' if smallSprocket else '1'}</sub></var>) = {"<var>i</var> * <var>Z<sub>1</sub></var>" if smallSprocket else "<span class='fraction'><span class='fup'><var>Z<sub>2</sub></var></span><span class='bar'>/</span><span class='fdn'><var>i</var></span></span>"}</span>
                           <p class='eq-c'>Number of teeth (<var>Z<sub>{'2' if smallSprocket else '1'}</sub></var>) = {f"{transmissionRatio} * {teethNumber}" if smallSprocket else f"<span class='fraction'><span class='fup'>{teethNumber}</span><span class='bar'>/</span><span class='fdn'>{transmissionRatio}</span></span>"}</p>
                           <p class='eq-c'>Number of teeth (<var>Z<sub>{'2' if smallSprocket else '1'}</sub></var>) = {teethNumber2}mm</p>
                           <br/>
                           
                           <p style='font-weight:bold;font-size:16px'>2. Determination of Sprockets Diameter</p>
                           <p class='eq-c'>Diameter 1 (<var>d<sub>1</sub></var>) = <span class='fraction'><span class='fup'><var>p</var></span><span class='bar'>/</span><span class='fdn'><var>sin(<span class='fraction'><span class='fup'>180</span><span class='bar'>/</span><span class='fdn'><var>z<sub>1</sub></var></span></span>)
                           </var></span></span></p>
                           <p class='eq-c'>Diameter 1 (<var>d<sub>1</sub></var>) = <span class='fraction'><span class='fup'><var>{pitch}</var></span><span class='bar'>/</span><span class='fdn'><var>sin(<span class='fraction'><span class='fup'>180</span><span class='bar'>/</span><span class='fdn'>{teethNumber if smallSprocket else teethNumber2}</span></span>)
                           </var></span></span></p>
                           <p>Diameter 1 (<var>d<sub>1</sub></var>) = {sprocket_diameter1}mm</p>
                           <p class='eq-c'>Diameter 2 (<var>d<sub>2</sub></var>) = <span class='fraction'><span class='fup'><var>p</var></span><span class='bar'>/</span><span class='fdn'><var>sin(<span class='fraction'><span class='fup'>180</span><span class='bar'>/</span><span class='fdn'><var>z<sub>2</sub></var></span></span>)
                           </var></span></span></p>
                           <p class='eq-c'>Diameter 2 (<var>d<sub>2</sub></var>) = <span class='fraction'><span class='fup'><var>{pitch}</var></span><span class='bar'>/</span><span class='fdn'><var>sin(<span class='fraction'><span class='fup'>180</span><span class='bar'>/</span><span class='fdn'>{teethNumber2 if smallSprocket else teethNumber}</span></span>)
                           </var></span></span></p>
                           <p>Diameter 2 (<var>d<sub>1</sub></var>) = {sprocket_diameter2}mm</p>
                           <br/>
                           
                           <p style='font-weight:bold;font-size:16px'>3. Determination of Design Power</p>
                           <p class='eq-c'>Design Power (<var>P<sub>d</sub></var>) = <var>P<sub>R</sub></var> * <var>K<sub>s</sub></var></p>
                           <p class='eq-c'>Design Power (<var>P<sub>d</sub></var>) = {ratedPower} * {serviceFactor}></p>
                           <p>Design Power (<var>P<sub>d</sub></var>) = {design_power}kW</p>
                           <br />
                           
                           <p style='font-weight:bold;font-size:16px'>4. Determination of Number of Links</p>
                           <p class='eq-c'>Number of links (<var>L<sub>n</sub></var>) = 2(<span class='fraction'><span class='fup'><var>a<sub>p</sub></var></span><span class='bar'>/</span><span class='fdn'><var>p</var></span></span>) + (<span class='fraction'><span class='fup'><var>z<sub>1</sub></var> + <var>z<sub>2</sub></var></span><span class='bar'>/</span><span class='fdn'>2</span></span>) + (<span class='fraction'><span class='fup'><var>z<sub>2</sub></var> - <var>z<sub>1</sub></var></span><span class='bar'>/</span><span class='fdn'>2π</span></span>)<sup>2</sup> * (<span class='fraction'><span class='fup'><var>p</var></span><span class='bar'>/</span><span class='fdn'><var>a<sub>p</sub></var></span></span>)</p>
                           <p class='eq-c'>Number of links (<var>L<sub>n</sub></var>) = {f"2(<span class='fraction'><span class='fup'>{centerDistance}</span><span class='bar'>/</span><span class='fdn'>{pitch}</span></span>) + (<span class='fraction'><span class='fup'>{teethNumber if smallSprocket else teethNumber2} + {teethNumber2 if smallSprocket else teethNumber}</span><span class='bar'>/</span><span class='fdn'>2</span></span>) + (<span class='fraction'><span class='fup'>{teethNumber2 if smallSprocket else teethNumber} - {teethNumber if smallSprocket else teethNumber2}</span><span class='bar'>/</span><span class='fdn'>2π</span></span>)<sup>2</sup> * (<span class='fraction'><span class='fup'>{pitch}</span><span class='bar'>/</span><span class='fdn'>{centerDistance}</span></span>)"}</p>
                           <p>Number of links (<var>L<sub>n</sub></var>) = {number_links}</p>
                           <br />
                           
                           <p style='font-weight:bold;font-size:16px'>5. Determination of Final Centre Distance</p>
                           <p class='eq-c'>Final Centre Distance (<var>a</var>) = <span class='fraction'><span class='fup'><var>p</var></span><span class='bar'>/</span><span class='fdn'>4</span></span>{{[<var>L<sub>n</sub></var> - (<span class='fraction'><span class='fup'><var>z<sub>1</sub></var> + <var><var>z<sub>2</sub></var></span><span class='bar'>/</span><span class='fdn'>2</span></span>)] + <span class="radical">√</span><span class="radicand"><var>[<var>L<sub>n</sub></var> - (<span class='fraction'><span class='fup'><var>z<sub>1</sub></var> + <var><var>z<sub>2</sub></var></span><span class='bar'>/</span><span class='fdn'>2</span></span>)]<sup>2</sup> - 8[<span class='fraction'><span class='fup'><var>z<sub>2</sub></var> - <var><var>z<sub>1</sub></var></span><span class='bar'>/</span><span class='fdn'>2π</span></span>]<sup>2</sup></var></span>}}</p>
                           <p class='eq-c'>Final Centre Distance (<var>a</var>) = <span class='fraction'><span class='fup'><var>p</var></span><span class='bar'>/</span><span class='fdn'>4</span></span>{{[{number_links} - (<span class='fraction'><span class='fup'>{teethNumber if smallSprocket else teethNumber2} + {teethNumber2 if smallSprocket else teethNumber}</span><span class='bar'>/</span><span class='fdn'>2</span></span>)] + <span class="radical">√</span><span class="radicand">[{number_links} - (<span class='fraction'><span class='fup'>{teethNumber if smallSprocket else teethNumber2} + {teethNumber2 if smallSprocket else teethNumber}</span><span class='bar'>/</span><span class='fdn'>2</span></span>)]<sup>2</sup> - 8[<span class='fraction'><span class='fup'>{teethNumber2 if smallSprocket else teethNumber} - {teethNumber if smallSprocket else teethNumber2}</span><span class='bar'>/</span><span class='fdn'>2π</span></span>]<sup>2</sup></span>}}</p>
                           <p>Final Centre Distance (<var>a</var>) = {final_center}</p>
                           <p>In order to accommodate initial sag in the chain, the value of centre distance is reduced by 2 to 5mm. therefore,</p>                           
                           <p>Final Centre Distance (<var>a</var>) = {final_center} - {int(initialSag)}</p>
                           <p>Final Centre Distance (<var>a</var>) = {round(final_center - int(initialSag))}mm</p>
                           <br />
                           
                           <p style='font-weight:bold;font-size:16px'>6. Determination of Length of Chain</p>
                           <p class='eq-c'>Length of Chain (<var>L<sub>p</sub></var>) = P{{2(<span class='fraction'><span class='fup'><var>a<sub>p</sub></var></span><span class='bar'>/</span><span class='fdn'><var>p</var></span></span>) + (<span class='fraction'><span class='fup'><var>z<sub>1</sub></var> + <var>z<sub>2</sub></var></span><span class='bar'>/</span><span class='fdn'>2</span></span>) + (<span class='fraction'><span class='fup'><var>z<sub>2</sub></var> - <var>z<sub>1</sub></var></span><span class='bar'>/</span><span class='fdn'>2π</span></span>)<sup>2</sup> * (<span class='fraction'><span class='fup'><var>p</var></span><span class='bar'>/</span><span class='fdn'><var>a<sub>p</sub></var></span></span>)}}</p>
                           <p class='eq-c'>Length of Chain (<var>L<sub>p</sub></var>) = <var>L<sub>n</sub></var> * <var>P</var> </p>
                           <p class='eq-c'>Length of Chain (<var>L<sub>p</sub></var>) = {number_links} * {pitch} </p>
                           <p class='eq-c'>Length of Chain (<var>L<sub>p</sub></var>) = {chain_length}mm </p>
                           <p class='eq-c'>Length of Chain (<var>L<sub>p</sub></var>) = {round_to_1_sf(round(chain_length))/1000}m </p>
                           <br />
                           
                           <p style='font-weight:bold;font-size:16px'>7. Determination of Velocity of Chain</p>
                           <p class='eq-c'>Velocity of Chain (<var>V</var>) = <span class='fraction'><span class='fup'><var>πDn<sub>1</sub></var></span><span class='bar'>/</span><span class='fdn'>60 * 1000</span></span></p>
                           <p class='eq-c'>Velocity of Chain (<var>V</var>) =  <span class='fraction'><span class='fup'><var>π * {sprocket_diameter1 if smallSprocket else sprocket_diameter2} * {rev1}</var></span><span class='bar'>/</span><span class='fdn'>60 * 1000</span></span></p>
                           <p class='eq-c'>Velocity of Chain (<var>V</var>) =  {chain_velocity}m/s</p>
                           <br />
                           
                           <p style='font-weight:bold;font-size:16px'>8. Determination of Load on the Chain</p>
                           <p class='eq-c'>Load on the Chain (<var>W</var>) = <span class='fraction'><span class='fup'><var>P<sub>R</sub></var></span><span class='bar'>/</span><span class='fdn'><var>V</var></span></span></p>
                           <p class='eq-c'>Load on the Chain (<var>W</var>) = <span class='fraction'><span class='fup'>{ratedPower}</span><span class='bar'>/</span><span class='fdn'>{chain_velocity}</span></span></p>
                           <p class='eq-c'>Load on the Chain (<var>W</var>) = {chain_load}kN = {chain_load*1000}N</p>
                           <br />
                           
                           <p style='font-weight:bold;font-size:16px'>9. Determination of Factor of Safety</p>
                           <p class='eq-c'>Factor of Safety (<var>n</var>) = <span class='fraction'><span class='fup'><var>Q</var></span><span class='bar'>/</span><span class='fdn'><var>W</var></span></span></p>
                           <p class='eq-c'>Factor of Safety (<var>n</var>) = <span class='fraction'><span class='fup'>{breakingLoad}</span><span class='bar'>/</span><span class='fdn'>{chain_load*1000}</span></span></p>
                           <p class='eq-c'>Factor of Safety (<var>n</var>) = {factor_of_safety}</p>
                           <br />
                           
                           <p style='font-weight:bold;font-size:16px'>10. Determination of Power transmitted by chain on the basis of Breaking Load</p>
                           <p class='eq-c'>Power transmitted by chain on the basis of Breaking Load (<var>N<sub>B</sub></var>) = <span class='fraction'><span class='fup'><var>Q.V</var></span><span class='bar'>/</span><span class='fdn'>102<var>nK<sub>s</sub></var></span></span></p>
                           <p class='eq-c'>Power transmitted by chain on the basis of Breaking Load (<var>N<sub>B</sub></var>) = <span class='fraction'><span class='fup'>{breakingLoad} * {chain_velocity}</span><span class='bar'>/</span><span class='fdn'>102 * {factor_of_safety} * {serviceFactor}</span></span></p>
                           <p class='eq-c'>Power transmitted by chain on the basis of Breaking Load (<var>N<sub>B</sub></var>) = {breaking_power}W</p>
                           <br />
                           
                           <p style='font-weight:bold;font-size:16px'>11. Determination of Power transmitted by chain on the basis of Bearing Load</p>
                           <p class='eq-c'>Power transmitted by chain on the basis of Bearing Load (<var>N<sub>B</sub></var>) = <span class='fraction'><span class='fup'><var>σ.A.V</var></span><span class='bar'>/</span><span class='fdn'>102<var>K<sub>s</sub></var></span></span></p>
                           <p class='eq-c'>Bearing Load (<var>σ</var>) = <span class='fraction'><span class='fup'><var>W</var></span><span class='bar'>/</span><span class='fdn'><var>A</var></span></span></p>
                           <p class='eq-c'>Bearing Load (<var>σ</var>) = <span class='fraction'><span class='fup'>{chain_load*1000}</span><span class='bar'>/</span><span class='fdn'><var>{bearingArea}</var></span></span></p>
                           <p class='eq-c'>Bearing Load (<var>σ</var>) = {bearing_load}</span></p>
                           
                           <p class='eq-c'>Power transmitted by chain on the basis of Bearing Load (<var>N<sub>B</sub></var>) = <span class='fraction'><span class='fup'>{bearing_load} * {bearingArea} * {chain_velocity}</span><span class='bar'>/</span><span class='fdn'>102 * {serviceFactor}</span></span></p>
                           <p class='eq-c'>Power transmitted by chain on the basis of Bearing Load (<var>N<sub>B</sub></var>) = {bearing_power}W</p>
                           <br />
                           
                           <p style='font-weight:bold;font-size:16px'>12. Determination of Total Tension on the driving side of the chain</p>
                           <p class='eq-c'>Total Tension (<span class="sum-frac">&sum;</span><var>F<sub>T</sub></var>) = <var>F<sub>t</sub> + <var>F<sub>c</sub> + <var>F<sub>s</sub></p>
                           
                           <p class='eq-c'>Tangential Driving Force (<var>F<sub>t</sub></var>) = <span class='fraction'><span class='fup'>102<var>P<sub>d</sub></var></span><span class='bar'>/</span><span class='fdn'><var>V</var></span></span></p>
                           <p class='eq-c'>Tangential Driving Force (<var>F<sub>t</sub></var>) = <span class='fraction'><span class='fup'>102 * {design_power}</var></span><span class='bar'>/</span><span class='fdn'><var>{chain_velocity}</var></span></span></p>
                           <p class='eq-c'>Tangential Driving Force (<var>F<sub>t</sub></var>) = {tangential_force}N</p>
                           
                           <p class='eq-c'>Centrifugal Tension (<var>F<sub>t</sub></var>) = m.V<sup>2</sup></p>
                           <p class='eq-c'>Centrifugal Tension (<var>F<sub>t</sub></var>) = {mass} * {chain_velocity}<sup>2</sup></p>
                           <p class='eq-c'>Centrifugal Tension (<var>F<sub>t</sub></var>) = {centrifugal_tension}N</p>
                                                      
                           <p class='eq-c'>Tension due to sagging (<var>F<sub>s</sub></var>) = K.m.g.a</p>
                           <p class='eq-c'>Tension due to sagging (<var>F<sub>s</sub></var>) = {constant} * {mass} * 9.8 * {final_center/1000}</p>
                           <p class='eq-c'>Tension due to sagging (<var>F<sub>s</sub></var>) = {sagging_tension}N</p>
                           
                           <p class='eq-c'>Total Tension (<span class="sum-frac">&sum;</span><var>F<sub>T</sub></var>) = {tangential_force} + {centrifugal_tension} + {sagging_tension}</p>                           
                           <p class='eq-c'>Total Tension (<span class="sum-frac">&sum;</span><var>F<sub>T</sub></var>) = {total_tension}N</p>
                           <br />
                           
                           <p style='font-weight:bold;font-size:16px'>13. Determination of Load on the haft</p>
                           <p class='eq-c'>Load on shaft (<var>Q<sub>s</sub></var>) = <var>F<sub>t</sub>.K<sub>t</sub></var></p>
                           <p class='eq-c'>Load on shaft (<var>Q<sub>s</sub></var>) = {tangential_force} * {loadFactor}</p>
                           <p class='eq-c'>Load on shaft (<var>Q<sub>s</sub></var>) = {shaft_load}N</p>
                           
                       """)
        except Exception as e:
            QMessageBox.critical(
                self, "App Error", str(e) if not hasattr(e, 'message') else str(e.message))
            return


lpBuffer = wintypes.LPWSTR()
AppUserModelID = ctypes.windll.shell32.GetCurrentProcessExplicitAppUserModelID
AppUserModelID(ctypes.cast(ctypes.byref(lpBuffer), wintypes.LPWSTR))
appid = lpBuffer.value
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(u"appid")

app = QApplication(sys.argv)
y = BeltWindow()
if getattr(sys, 'frozen', False):
    pyi_splash.close()
y.show()
app.exec()
