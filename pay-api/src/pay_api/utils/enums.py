# Copyright © 2019 Province of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Enum definitions."""
from enum import Enum


class AuthHeaderType(Enum):
    """Authorization header types."""

    BASIC = 'Basic {}'
    BEARER = 'Bearer {}'


class ContentType(Enum):
    """Http Content Types."""

    JSON = 'application/json'
    FORM_URL_ENCODED = 'application/x-www-form-urlencoded'
    CSV = 'text/csv'
    PDF = 'application/pdf'


class PaymentStatus(Enum):
    """Payment status codes."""

    CREATED = 'CREATED'
    COMPLETED = 'COMPLETED'
    DELETED = 'DELETED'
    DELETE_ACCEPTED = 'DELETE_ACCEPTED'


class InvoiceStatus(Enum):
    """Invoice status codes."""

    CREATED = 'CREATED'
    PAID = 'PAID'
    DELETED = 'DELETED'


class TransactionStatus(Enum):
    """Transaction status codes."""

    CREATED = 'CREATED'
    COMPLETED = 'COMPLETED'
    FAILED = 'FAILED'
    CANCELLED = 'CANCELLED'
    EVENT_FAILED = 'EVENT_FAILED'


class LineItemStatus(Enum):
    """Line Item status codes."""

    ACTIVE = 'ACTIVE'
    CANCELLED = 'CANCELLED'


class InvoiceReferenceStatus(Enum):
    """Line Invoice Reference status codes."""

    ACTIVE = 'ACTIVE'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'


class PaymentSystem(Enum):
    """Payment System Codes."""

    PAYBC = 'PAYBC'
    BCOL = 'BCOL'
    INTERNAL = 'INTERNAL'


class Role(Enum):
    """User Role."""

    BASIC = 'basic'
    PREMIUM = 'premium'
    STAFF = 'staff'
    VIEWER = 'view'
    EDITOR = 'edit'
    SYSTEM = 'system'


class Code(Enum):
    """Code value keys."""

    ERROR = 'errors'
    PAYMENT_STATUS = 'payment_statuses'


class AccountType(Enum):
    """Account types."""

    BASIC = 'BASIC'
    PREMIUM = 'PREMIUM'
