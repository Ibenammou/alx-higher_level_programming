#define PY_SSIZE_T_CLEAN
#include <Python.h>

void print_python_list(PyObject *p) {
    Py_ssize_t i, size;
    PyObject *item;

    if (PyList_Check(p)) {
        size = PyList_Size(p);
        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %ld\n", size);
        printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
        for (i = 0; i < size; i++) {
            item = PyList_GetItem(p, i);
            printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
            if (PyBytes_Check(item)) {
                printf("[.] bytes object info\n");
                printf("  size: %ld\n", PyBytes_GET_SIZE(item));
                printf("  trying string: %s\n", PyBytes_AsString(item));
                printf("  first %d bytes: ", (int)PyBytes_GET_SIZE(item) < 10 ? (int)PyBytes_GET_SIZE(item) : 10);
                for (int j = 0; j < (int)PyBytes_GET_SIZE(item) && j < 10; j++) {
                    printf("%02x ", ((unsigned char *)PyBytes_AsString(item))[j]);
                }
                printf("\n");
            }
        }
    } else {
        printf("[ERROR] Invalid Python List\n");
    }
}

void print_python_bytes(PyObject *p) {
    if (PyBytes_Check(p)) {
        printf("[.] bytes object info\n");
        printf("  size: %ld\n", PyBytes_GET_SIZE(p));
        printf("  trying string: %s\n", PyBytes_AsString(p));
        printf("  first %d bytes: ", (int)PyBytes_GET_SIZE(p) < 10 ? (int)PyBytes_GET_SIZE(p) : 10);
        for (int i = 0; i < (int)PyBytes_GET_SIZE(p) && i < 10; i++) {
            printf("%02x ", ((unsigned char *)PyBytes_AsString(p))[i]);
        }
        printf("\n");
    } else {
        printf("[ERROR] Invalid Bytes Object\n");
    }
}

int main(void) {
    Py_Initialize();
    PyObject *s = PyBytes_FromString("Hello");
    PyObject *b = PyBytes_FromString("\xff\xf8\x00\x00\x00\x00\x00\x00");
    PyObject *l = PyList_New(0);
    
    print_python_bytes(s);
    print_python_bytes(b);
    print_python_list(l);

    Py_DECREF(s);
    Py_DECREF(b);
    Py_DECREF(l);
    Py_Finalize();
    return (0);
}

