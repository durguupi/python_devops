# Simple script to remove .srt files in my folder
import os

directory = '/mnt/e/microsoft_azure/HashicorpTerraformAssociateCertificationPreparationGuide/HashicorpTerraformPreparationGuide/PARTICORECONCEPTTerraformCore'

test = os.listdir(directory)

# for item in test:
#     print(item)

for item in test:
    if item.endswith('.srt'):
        # print(item)
        os.remove(os.path.join(directory, item))

print(test)
