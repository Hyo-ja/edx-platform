"""
Toggles for instructor app
"""

from openedx.core.djangoapps.waffle_utils import WaffleFlagNamespace, WaffleFlag

# Namespace for instructor waffle flags.
WAFFLE_FLAG_NAMESPACE = WaffleFlagNamespace(name='instructor')

# Waffle flag to use improved is_small_course.
# .. toggle_name: verify_student.improved_is_small_course
# .. toggle_implementation: WaffleFlag
# .. toggle_default: False
# .. toggle_description: Supports staged rollout to improved is_small_course method.
# .. toggle_category: instructor
# .. toggle_use_cases: incremental_release, open_edx
# .. toggle_creation_date: 2020-07-02
# .. toggle_expiration_date: n/a
# .. toggle_warnings: n/a
# .. toggle_tickets: PROD-1740
# .. toggle_status: supported
IMPROVED_IS_SMALL_COURSE = WaffleFlag(
    waffle_namespace=WAFFLE_FLAG_NAMESPACE,
    flag_name='improved_is_small_course',
    flag_undefined_default=False
)


def use_improved_is_small_course():
    return IMPROVED_IS_SMALL_COURSE.is_enabled()
