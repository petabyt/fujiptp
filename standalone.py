import ptpy
from construct import Container

def custom(self, code, param = []):
    ptp = Container(
        OperationCode=code,
        SessionID=self._session,
        TransactionID=self._transaction,
        Parameter=param
    )

    response = self.recv(ptp)
    return response

setattr(ptpy.PTP, "custom_recv", custom)

camera = ptpy.PTPy()

with camera.session():
    print(camera.custom_recv("GetThumb", [0, 0]))
