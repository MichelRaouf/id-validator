from django.test import TestCase
from id_validator.utils import validate_national_id

class NationalIDValidationTests(TestCase):

    def test_valid_id_1900s(self):
        """Test a valid ID belonging to a male born in the 1900s"""
        is_valid, result = validate_national_id("29901010101231")
        self.assertTrue(is_valid)
        self.assertEqual(result["birth_date"], "1999-01-01")

    def test_valid_id_2000s(self):
        """Test a valid ID belonging to a female born in the 2000s"""
        is_valid, result = validate_national_id("30405260302262")
        self.assertTrue(is_valid)
        self.assertEqual(result["birth_date"], "2004-05-26")

    def test_invalid_length(self):
        """Test ID with incorrect length (not 14 digits)"""
        is_valid, message = validate_national_id("12345")
        self.assertFalse(is_valid)
        self.assertEqual(message, "Invalid format. The ID must be 14 digits.")

    def test_non_numeric_id(self):
        """Test ID containing non-numeric characters"""
        is_valid, message = validate_national_id("299A1020301456")
        self.assertFalse(is_valid)
        self.assertEqual(message, "Invalid format. The ID must be 14 digits.")

    def test_invalid_century_code(self):
        """Test ID with an invalid century code"""
        is_valid, message = validate_national_id("49901020301456")
        self.assertFalse(is_valid)
        self.assertEqual(message, "Invalid century code in ID.")

    def test_invalid_birth_date(self):
        """Test ID with an impossible birth date"""
        is_valid, message = validate_national_id("29902310201456")
        self.assertFalse(is_valid)
        self.assertEqual(message, "Invalid birth date in ID.")

    def test_valid_id_cairo(self):
        """Test ID belonging to someone born in Cairo (code 01)"""
        is_valid, result = validate_national_id("30001020101456")
        self.assertTrue(is_valid)
        self.assertEqual(result["governorate"], "Cairo")

    def test_valid_id_alexandria(self):
        """Test ID belonging to someone born in Alexandria (code 02)"""
        is_valid, result = validate_national_id("30001020201456")
        self.assertTrue(is_valid)
        self.assertEqual(result["governorate"], "Alexandria")

    def test_valid_id_port_said(self):
        """Test ID belonging to someone born in Port Said (code 03)"""
        is_valid, result = validate_national_id("30001020301456")
        self.assertTrue(is_valid)
        self.assertEqual(result["governorate"], "Port Said")

    def test_valid_id_suez(self):
        """Test ID belonging to someone born in Suez (code 04)"""
        is_valid, result = validate_national_id("30001020401456")
        self.assertTrue(is_valid)
        self.assertEqual(result["governorate"], "Suez")

    def test_valid_id_damietta(self):
        """Test ID belonging to someone born in Damietta (code 11)"""
        is_valid, result = validate_national_id("30001021101456")
        self.assertTrue(is_valid)
        self.assertEqual(result["governorate"], "Damietta")

    def test_valid_id_dakahlia(self):
        """Test ID belonging to someone born in Dakahlia (code 12)"""
        is_valid, result = validate_national_id("30001021201456")
        self.assertTrue(is_valid)
        self.assertEqual(result["governorate"], "Dakahlia")

    def test_valid_id_sharqia(self):
        """Test ID belonging to someone born in Sharqia (code 13)"""
        is_valid, result = validate_national_id("30001021301456")
        self.assertTrue(is_valid)
        self.assertEqual(result["governorate"], "Sharqia")

    def test_valid_id_qalyubia(self):
        """Test ID belonging to someone born in Qalyubia (code 14)"""
        is_valid, result = validate_national_id("30001021401456")
        self.assertTrue(is_valid)
        self.assertEqual(result["governorate"], "Qalyubia")

    def test_valid_id_kafr_el_sheikh(self):
        """Test ID belonging to someone born in Kafr El Sheikh (code 15)"""
        is_valid, result = validate_national_id("30001021501456")
        self.assertTrue(is_valid)
        self.assertEqual(result["governorate"], "Kafr El Sheikh")

    def test_valid_id_gharbia(self):
        """Test ID belonging to someone born in Gharbia (code 16)"""
        is_valid, result = validate_national_id("30001021601456")
        self.assertTrue(is_valid)
        self.assertEqual(result["governorate"], "Gharbia")

    def test_valid_id_monufia(self):
        """Test ID belonging to someone born in Monufia (code 17)"""
        is_valid, result = validate_national_id("30001021701456")
        self.assertTrue(is_valid)
        self.assertEqual(result["governorate"], "Monufia")

    def test_valid_id_beheira(self):
        """Test ID belonging to someone born in Beheira (code 18)"""
        is_valid, result = validate_national_id("30001021801456")
        self.assertTrue(is_valid)
        self.assertEqual(result["governorate"], "Beheira")

    def test_valid_id_ismailia(self):
        """Test ID belonging to someone born in Ismailia (code 19)"""
        is_valid, result = validate_national_id("30001021901456")
        self.assertTrue(is_valid)
        self.assertEqual(result["governorate"], "Ismailia")

    def test_valid_id_giza(self):
        """Test ID belonging to someone born in Giza (code 21)"""
        is_valid, result = validate_national_id("30001022101456")
        self.assertTrue(is_valid)
        self.assertEqual(result["governorate"], "Giza")

    def test_valid_id_beni_suef(self):
        """Test ID belonging to someone born in Beni Suef (code 22)"""
        is_valid, result = validate_national_id("30001022201456")
        self.assertTrue(is_valid)
        self.assertEqual(result["governorate"], "Beni Suef")

    def test_valid_id_fayoum(self):
        """Test ID belonging to someone born in Fayoum (code 23)"""
        is_valid, result = validate_national_id("30001022301456")
        self.assertTrue(is_valid)
        self.assertEqual(result["governorate"], "Fayoum")

    def test_valid_id_minya(self):
        """Test ID belonging to someone born in Minya (code 24)"""
        is_valid, result = validate_national_id("30001022401456")
        self.assertTrue(is_valid)
        self.assertEqual(result["governorate"], "Minya")

    def test_valid_id_assiut(self):
        """Test ID belonging to someone born in Assiut (code 25)"""
        is_valid, result = validate_national_id("30001022501456")
        self.assertTrue(is_valid)
        self.assertEqual(result["governorate"], "Assiut")

    def test_valid_id_sohag(self):
        """Test ID belonging to someone born in Sohag (code 26)"""
        is_valid, result = validate_national_id("30001022601456")
        self.assertTrue(is_valid)
        self.assertEqual(result["governorate"], "Sohag")

    def test_valid_id_qena(self):
        """Test ID belonging to someone born in Qena (code 27)"""
        is_valid, result = validate_national_id("30001022701456")
        self.assertTrue(is_valid)
        self.assertEqual(result["governorate"], "Qena")

    def test_valid_id_aswan(self):
        """Test ID belonging to someone born in Aswan (code 28)"""
        is_valid, result = validate_national_id("30001022801456")
        self.assertTrue(is_valid)
        self.assertEqual(result["governorate"], "Aswan")

    def test_valid_id_luxor(self):
        """Test ID belonging to someone born in Luxor (code 29)"""
        is_valid, result = validate_national_id("30001022901456")
        self.assertTrue(is_valid)
        self.assertEqual(result["governorate"], "Luxor")

    def test_valid_id_red_sea(self):
        """Test ID belonging to someone born in Red Sea (code 31)"""
        is_valid, result = validate_national_id("30001023101456")
        self.assertTrue(is_valid)
        self.assertEqual(result["governorate"], "Red Sea")

    def test_valid_id_new_valley(self):
        """Test ID belonging to someone born in New Valley (code 32)"""
        is_valid, result = validate_national_id("30001023201456")
        self.assertTrue(is_valid)
        self.assertEqual(result["governorate"], "New Valley")

    def test_valid_id_matruh(self):
        """Test ID belonging to someone born in Matruh (code 33)"""
        is_valid, result = validate_national_id("30001023301456")
        self.assertTrue(is_valid)
        self.assertEqual(result["governorate"], "Matruh")

    def test_valid_id_north_sinai(self):
        """Test ID belonging to someone born in North Sinai (code 34)"""
        is_valid, result = validate_national_id("30001023401456")
        self.assertTrue(is_valid)
        self.assertEqual(result["governorate"], "North Sinai")

    def test_valid_id_south_sinai(self):
        """Test ID belonging to someone born in South Sinai (code 35)"""
        is_valid, result = validate_national_id("30001023501456")
        self.assertTrue(is_valid)
        self.assertEqual(result["governorate"], "South Sinai")

    def test_valid_id_outside_egypt(self):
        """Test ID belonging to someone born outside Egypt (code 88)"""
        is_valid, result = validate_national_id("30001028801456")
        self.assertTrue(is_valid)
        self.assertEqual(result["governorate"], "Outside Egypt")

    def test_unknown_governorate_code(self):
        """Test ID with an unlisted governorate code"""
        is_valid, result = validate_national_id("29901029901456")
        self.assertTrue(is_valid)
        self.assertEqual(result["governorate"], "Unknown")

    def test_gender_classification_male(self):
        """Test if gender is classified correctly for males"""
        is_valid, result = validate_national_id("29901020301451")
        self.assertTrue(is_valid)
        self.assertEqual(result["gender"], "Male")

    def test_gender_classification_female(self):
        """Test if gender is classified correctly for females"""
        is_valid, result = validate_national_id("29901020301442")
        self.assertTrue(is_valid)
        self.assertEqual(result["gender"], "Female")
