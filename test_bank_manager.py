# import unittest
# from unittest.mock import patch, MagicMock
# from main import BankManager  # Replace 'your_module' with the actual module name
#
#
# class TestBankManager(unittest.TestCase):
#     @patch('your_module.Details')
#     @patch('your_module.AccountManager')
#     def test_create_account_success(self, MockAccountManager, MockDetails):
#         # Setup mocks
#         mock_account = MagicMock()
#         MockAccountManager.create_account.return_value = mock_account
#         mock_details = MagicMock()
#         MockDetails.return_value = mock_details
#
#         bank_manager = BankManager()
#         result = bank_manager.create_account("John", "Doe", "john.doe@example.com", "Password123!", "Password123!")
#
#         self.assertEqual(result, "Account created successfully!")
#         MockDetails.assert_called_once_with(account_holder="John", surname="Doe", email="john.doe@example.com",
#                                             password="Password123!")
#         MockAccountManager.create_account.assert_called_once_with(mock_details)
#
#     @patch('your_module.AccountManager')
#     def test_sign_in_success(self, MockAccountManager):
#         mock_account = MagicMock()
#         MockAccountManager.sign_in.return_value = mock_account
#
#         bank_manager = BankManager()
#         result = bank_manager.sign_in("john.doe@example.com", "Password123!")
#
#         self.assertEqual(result, "Sign in successful!")
#         MockAccountManager.sign_in.assert_called_once_with("john.doe@example.com", "Password123!")
#
#     def test_menu_deposit(self):
#         bank_manager = BankManager()
#         bank_manager.account = MagicMock()
#
#         result = bank_manager.menu('1', 100.0)
#
#         self.assertEqual(result, "Deposit successful!")
#         bank_manager.account.deposit.assert_called_once_with(100.0)
#
#     def test_menu_invalid_choice(self):
#         bank_manager = BankManager()
#         result = bank_manager.menu('99')
#         self.assertEqual(result, "Invalid choice.")
#
#
# if __name__ == '__main__':
#     unittest.main()
