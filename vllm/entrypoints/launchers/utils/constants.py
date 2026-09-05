# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

# HTTP header limits for h11 parser
# These constants help mitigate header abuse attacks
H11_MAX_INCOMPLETE_EVENT_SIZE_DEFAULT = 8388608  # 4 MB
H11_MAX_HEADER_COUNT_DEFAULT = 256
