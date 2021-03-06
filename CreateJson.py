from body.KeyPoints import *
import codecs, json
import numpy as np
import os

class CreateJson():

    def __init__(self, kp, img_id, nameEx):
        self.kp = kp
        self.img_id = img_id
        self.nameEx = nameEx

        # print(KeyPoints.getBodyKeypoints(self.kp))

        BodyKey = np.array([[KeyPoints.getNeck1(kp), KeyPoints.getNeck2(kp)],
                            [KeyPoints.getRShoulder1(kp), KeyPoints.getRShoulder2(kp)],
                            [KeyPoints.getRElbow1(kp), KeyPoints.getRElbow1(kp)],
                            [KeyPoints.getRWrist1(kp), KeyPoints.getRWrist2(kp)],
                            [KeyPoints.getLShoulder1(kp), KeyPoints.getLShoulder2(kp)],
                            [KeyPoints.getLElbow1(kp), KeyPoints.getLElbow2(kp)],
                            [KeyPoints.getLWrist1(kp), KeyPoints.getLWrist2(kp)],
                            [KeyPoints.getMidHip1(kp), KeyPoints.getMidHip2(kp)],
                            [KeyPoints.getRHip1(kp), KeyPoints.getRHip2(kp)],
                            [KeyPoints.getRKnee1(kp), KeyPoints.getRKnee2(kp)],
                            [KeyPoints.getRAnkle1(kp), KeyPoints.getRAnkle2(kp)],
                            [KeyPoints.getLHip1(kp), KeyPoints.getLHip2(kp)],
                            [KeyPoints.getLKnee1(kp), KeyPoints.getLKnee2(kp)],
                            [KeyPoints.getLAnkle1(kp), KeyPoints.getLAnkle2(kp)]])
        # print(BodyKey)
        # print(BodyKey.shape)
        try:

            # json
            b = BodyKey.tolist()
            print('Write__>>', self.nameEx + '/keypose', + self.img_id)
            file_path = ('dataSet/' + str(self.nameEx) + '/keypose.' + str(self.img_id) + ".json")
            if self.nameEx == 'cam':
                json.dump(b, codecs.open(file_path, 'wb', encoding='utf-8'), separators=(',', ':'), sort_keys=True,
                          indent=4)
            else:
                json.dump(b, codecs.open(file_path, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True,
                          indent=4)
            # key = open('keypose.json','a')
        except  IOError as e:
            print(e)
