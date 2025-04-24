#include "number.h"
#include <algorithm>
#include <cstring>

uint2022_t from_uint(uint32_t i) {
    uint2022_t result;
    memset(result.data, 0, sizeof(result.data));
    result.size = 1;
    result.data[0] = i;
    return result;
}

uint2022_t from_string(const char* buff) {
    uint2022_t result;
    memset(result.data, 0, sizeof(result.data));
    result.size = 1;
    result.data[0] = 0;

    while (*buff >= '0' && *buff <= '9') {
        result.data[0] = result.data[0] * 10 + (*buff - '0');
        buff++;
    }

    return result;
}

uint2022_t operator+(const uint2022_t& lhs, const uint2022_t& rhs) {
    uint2022_t result;
    memset(result.data, 0, sizeof(result.data));
    result.size = std::max(lhs.size, rhs.size);
    uint32_t carry = 0;

    for (int i = 0; i < result.size; i++) {
        uint64_t sum = (uint64_t)lhs.data[i] + rhs.data[i] + carry;
        result.data[i] = sum & 0xFFFFFFFF;
        carry = sum >> 32;
    }

    if (carry) {
        result.data[result.size] = carry;
        result.size++;
    }

    return result;
}

uint2022_t operator-(const uint2022_t& lhs, const uint2022_t& rhs) {
    uint2022_t result;
    memset(result.data, 0, sizeof(result.data));
    result.size = lhs.size;
    uint32_t borrow = 0;

    for (int i = 0; i < result.size; i++) {
        uint64_t diff = (uint64_t)lhs.data[i] - rhs.data[i] - borrow;
        result.data[i] = diff & 0xFFFFFFFF;
        borrow = (diff >> 32) ? 1 : 0;
    }

    return result;
}

uint2022_t operator*(const uint2022_t& lhs, const uint2022_t& rhs) {
    uint2022_t result;
    memset(result.data, 0, sizeof(result.data));
    result.size = lhs.size + rhs.size;

    for (int i = 0; i < lhs.size; i++) {
        uint32_t carry = 0;
        for (int j = 0; j < rhs.size; j++) {
            uint64_t product = (uint64_t)lhs.data[i] * rhs.data[j] + result.data[i + j] + carry;
            result.data[i + j] = product & 0xFFFFFFFF;
            carry = product >> 32;
        }
        if (carry) {
            result.data[i + rhs.size] += carry;
        }
    }

    while (result.size > 1 && result.data[result.size - 1] == 0) {
        result.size--;
    }

    return result;
}

uint2022_t operator/(const uint2022_t& lhs, const uint2022_t& rhs) {
    if (rhs == from_uint(0)) {
        throw std::runtime_error("Division by zero!");
    }

    uint2022_t quotient = from_uint(0);  // Результат
    uint2022_t remainder = lhs;          // Остаток

    // Проверка, что остаток не меньше делителя
    while (!(remainder < rhs)) {
        remainder = remainder - rhs;
        quotient = quotient + from_uint(1);
    }

    return quotient;
}

bool operator<(const uint2022_t& lhs, const uint2022_t& rhs) {
	if (lhs.size != rhs.size) return lhs.size < rhs.size;
	for (int i = lhs.size - 1; i >= 0; i--) {
		if (lhs.data[i] != rhs.data[i]) return lhs.data[i] < rhs.data[i];
	}
	return false;
}

bool operator==(const uint2022_t& lhs, const uint2022_t& rhs) {
    if (lhs.size != rhs.size) return false;
    for (int i = 0; i < lhs.size; i++) {
        if (lhs.data[i] != rhs.data[i]) return false;
    }
    return true;
}

bool operator!=(const uint2022_t& lhs, const uint2022_t& rhs) {
    return !(lhs == rhs);
}

std::ostream& operator<<(std::ostream& stream, const uint2022_t& value) {
    if (value.size == 1) {
        stream << value.data[0];
    }
    else {
        for (int i = value.size - 1; i >= 0; i--) {
            stream << value.data[i];
        }
    }
    return stream;
}