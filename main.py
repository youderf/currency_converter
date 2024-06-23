
# Auteur: Younes Derfoufi, docteur agrégé 
# Formateur des enseignants stagiaires au CRMEF OUJDA

# Site Web : https://www.tresfacile.net/
# Youtube  : https://www.youtube.com/user/InformatiquesFacile
# Facebook : https://www.facebook.com/almoubarayate/

import sys
from library import *
from exchangeConverter import *

def btn_action():
    base_currency = ui.comboBox_base_currency.currentText()
    target_currency = ui.comboBox_target_currency.currentText()
    amount = float(ui.lineEdit_base_currency.text())
    convert_value = convert_currency(base_currency, target_currency, amount)
    convert_value = str(convert_value)
    ui.lineEdit_target_value.setText(convert_value)

    # Compute currency exchange rate
    exchange_rate = str(convert_currency(base_currency, target_currency, 1))
    ui.lbl_result.setText(exchange_rate)



app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)

data_exchange = get_exchange_rates('USD')['rates']
ui.comboBox_base_currency.addItems(list(data_exchange.keys()))
ui.comboBox_target_currency.addItems(list(data_exchange.keys()))
base_currency = ui.lineEdit_base_currency.text()
target_currency = ui.lineEdit_target_value.text()
ui.btn_validate.clicked.connect(btn_action)


Form.show()
sys.exit(app.exec_())