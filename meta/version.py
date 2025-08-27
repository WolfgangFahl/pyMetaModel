"""
Created on 2023-02-19

@author: wf
"""

import meta


class Version(object):
    """
    Version handling for pyMetaModel
    """

    name = "pyMetaModel"
    description = "pyMetaModel: MetaModel for Knowledge Graphs"
    version = meta.__version__
    date = "2022-11-30"
    updated = "2025-08-27"
    authors = "Wolfgang Fahl"
    doc_url = "https://wiki.bitplan.com/index.php/pyMetaModel"
    chat_url = "https://github.com/WolfgangFahl/pyMetaModel/discussions"
    cm_url = "https://github.com/WolfgangFahl/pyMetaModel"
    license = f"""Copyright 2022-2025 contributors. All rights reserved.
  Licensed under the Apache License 2.0
  http://www.apache.org/licenses/LICENSE-2.0
  Distributed on an "AS IS" basis without warranties
  or conditions of any kind, either express or implied."""
    longDescription = f"""{name} version {version}
{description}
  Created by {authors} on {date} last updated {updated}"""
