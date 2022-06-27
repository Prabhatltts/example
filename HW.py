# Base libraries
import logging
import time

# external libs
import serial
from nose import tools
from time import sleep
import sys
import polling2

# Rakuten libs
from proj_lib import hw_diag_lib as hwd_lib
from docs import configs

# Global  constants
DEBUG_ENABLED = True
BYTES_COUNT = 500000

# Global
SERIAL_PORT = hwd_lib.SERIAL_PORT
BAUD_RATE = hwd_lib.BAUD_RATE
TIME_OUT = hwd_lib.TIME_OUT


class DiagTest(hwd_lib.SerialComm):
  def __init__(self):
    self.response = []
    self.du_data = ''
    #self.serial_comm_obj = HWD_lib.SerialComm

  def fetchSysInfo(self):
    hwd_lib.SerialComm.fetchSysInfo(self)

  def TestDDR(self):
    module = 'ddr'
    cmds = [b'ddr\r\n',b'test\r\n']
    response = ['test','PASSED']
    result = hwd_lib.SerialComm.TestExec(self, module, cmds, response, SERIAL_PORT, BAUD_RATE)
    return result

  def TestPower(self):
    module = 'power'
    cmds = [b'power\r\n',b'test_volt_pwr\r\n']
    response = ['test_volt_pwr','Power_Good']
    result = hwd_lib.serial_comm_obj.TestExec(module, cmds, response, SERIAL_PORT, BAUD_RATE)
    return result

  def TestDisp(self):
    module = 'power'
    cmds = [b'power\r\n',b'disp_volt_cur\r\n']
    response = ['disp_volt_cur', 'Display']
    result = hwd_lib.serial_comm_obj.TestExec(module, cmds, response, SERIAL_PORT, BAUD_RATE)
    return result

  def TestDispTemp(self):
    module = 'power'
    cmds = [b'power\r\n',b'disp_temp\r\n']
    response = ['disp_temp', 'temperature']
    result = hwd_lib.serial_comm_obj.TestExec(module, cmds, response, SERIAL_PORT, BAUD_RATE)
    return result

  def TestHelpClrErr(self):
    module = '\'help\''
    cmds = [b'help\r\n',b'clrerr\r\n']
    response = ['clrerr', 'clrerr']
    result = hwd_lib.serial_comm_obj.TestExec(module, cmds, response, SERIAL_PORT, BAUD_RATE)
    return result

  def TestHelpErrLog(self):
    module = '\'help\''
    cmds = [b'help\r\n',b'errlog\r\n']
    response = ['errlog', 'log']
    result = hwd_lib.serial_comm_obj.TestExec(module, cmds, response, SERIAL_PORT, BAUD_RATE)
    return result

  def TestHelpGrpadd(self):
    module = '\'help\''
    cmds = [b'help\r\n',b'grpadd\r\n']
    response = ['Help', '']
    result = hwd_lib.serial_comm_obj.TestExec(module, cmds, response, SERIAL_PORT, BAUD_RATE)
    return result

  def TestMissingModule(self):
    module = 'rack'
    cmds = [b'rack\r\n',b'rack_temp\r\n']
    response = ['rack', 'Rack Temperature']
    result = hwd_lib.serial_comm_obj.TestExec(module, cmds, response, SERIAL_PORT, BAUD_RATE)
    return result

  def TestDispTempMissingPort(self):
    module = 'power'
    cmds = [b'power\r\n']
    response = ['could not open port']
    result = hwd_lib.serial_comm_obj.TestExec(module, cmds, response, SERIAL_PORT, BAUD_RATE)
    return result

  def TestWrongBaudRate(self):
    module = 'power'
    cmds = [b'power\r\n',b'disp_temp\r\n']
    response = ['disp_temp', 'Display temperature utility']
    result = hwd_lib.serial_comm_obj.TestExec(module, cmds, response, SERIAL_PORT, BAUD_RATE)
    return result

  def TestGrpadd(self):
    module = '\'help\''
    cmds = [b'help\r\n',b'grpadd\r\n']
    response = ['grpadd', 'Do']
    result = hwd_lib.serial_comm_obj.TestExec(module, cmds, response, SERIAL_PORT, BAUD_RATE)
    return result

  def TestGrpaddFile(self):
    module = '\'help\''
    cmds = [b'help\r\n', b'grpaddfile\r\n']
    response = ['grpshow', 'Do']
    result = hwd_lib.serial_comm_obj.TestExec(module, cmds, response, SERIAL_PORT, BAUD_RATE)
    return result

  def TestGrpshow(self):
    module = '\'help\''
    cmds = [b'help\r\n',b'grpshow\r\n']
    response = ['grpshow', 'Group']
    result = hwd_lib.serial_comm_obj.TestExec(module, cmds, response, SERIAL_PORT, BAUD_RATE)
    return result


  def TestGrpexec(self):
    module = '\'help\''
    cmds = [b'help\r\n', b'grpexec\r\n']
    response = ['grpexec', 'Do']
    result = hwd_lib.serial_comm_obj.TestExec(module, cmds, response, SERIAL_PORT, BAUD_RATE)
    return result

  def TestGrpdel(self):
    module = '\'help\''
    cmds = [b'help\r\n',b'grpdel\r\n']
    response = ['grpdel', 'Do']
    result = hwd_lib.serial_comm_obj.TestExec(module, cmds, response, SERIAL_PORT, BAUD_RATE)
    return result

  def TestHistory(self):
    module = '\'help\''
    cmds = [b'help\r\n',b'history\r\n']
    response = ['history', 'history']
    result = hwd_lib.serial_comm_obj.TestExec(module, cmds, response, SERIAL_PORT, BAUD_RATE)
    return result

  def TestIntver(self):
    module = '\'help\''
    cmds = [b'help\r\n',b'intver\r\n']
    response = ['history', 'Foxconn']
    #serial_comm_obj = HWD_lib.SerialComm()
    result = hwd_lib.serial_comm_obj.TestExec(module, cmds, response, SERIAL_PORT, BAUD_RATE)
    return result

  def TestLoopcnt(self):
    module = '\'help\''
    cmds = [b'help\r\n',b'loopcnt 5\r\n',b'ddr\r\n',b'test\r\n']
    response = ['history', 'Change','test','DDR']

    result = hwd_lib.serial_comm_obj.TestExec(module, cmds, response, SERIAL_PORT, BAUD_RATE)
    return result

  def Testversion(self):
    module = '\'help\''
    cmds = [b'help\r\n',b'version\r\n']
    response = ['history', 'Foxconn']
    result = hwd_lib.serial_comm_obj.TestExec(module, cmds, response, SERIAL_PORT, BAUD_RATE)
    return result

  def TestExit(self):
    module = '\'help\''
    cmds = [b'help\r\n',b'exit\r\n']
    response = ['history', 'exit']
    result = hwd_lib.serial_comm_obj.TestExec(module, cmds, response, SERIAL_PORT, BAUD_RATE)
    return result

  def TestSh(self):
    module = '\'help\''
    cmds = [b'help\r\n', b'sh\r\n']
    response = ['history','sh']
    result = hwd_lib.serial_comm_obj.TestExec(module, cmds, response, SERIAL_PORT, BAUD_RATE)
    return result


if __name__ == "__main__":
  diagTestObj = DiagTest()
  testRedLedOnStatus = False

  sysInfo = diagTestObj.fetchSysInfo()
  if sysInfo:
    print("System Information:",sysInfo)
  else:
    print("Failed to capture system information")


  testDDRStatus = diagTestObj.TestDDR()
  if testDDRStatus:
    print("DDR tested Successfully")
  else:
    print("DDR test failed")

  sys.exit()
